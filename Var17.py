import numpy as np
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class CollaborativeFiltering:
    def __init__(self, num_users, num_items, embedding_dim=16):
        self.num_users = num_users
        self.num_items = num_items
        self.embedding_dim = embedding_dim
        self.model = self._build_model()
    
    def _build_model(self):
        """Построение NCF модели с Matrix Factorization"""
        # Входы
        user_input = tf.keras.Input(shape=(), dtype=tf.int32, name='user_input')
        item_input = tf.keras.Input(shape=(), dtype=tf.int32, name='item_input')
        
        # Embedding слои для users и items
        user_embedding = tf.keras.layers.Embedding(self.num_users, self.embedding_dim, name='user_emb')(user_input)
        item_embedding = tf.keras.layers.Embedding(self.num_items, self.embedding_dim, name='item_emb')(item_input)
        
        # Bias слои
        user_bias = tf.keras.layers.Embedding(self.num_users, 1, name='user_bias')(user_input)
        item_bias = tf.keras.layers.Embedding(self.num_items, 1, name='item_bias')(item_input)
        
        # Matrix Factorization: dot product embeddings
        mf_output = tf.keras.layers.Dot(axes=1, name='mf_dot')([user_embedding, item_embedding])
        
        # NCF часть: Deep Neural Network
        concat = tf.keras.layers.Concatenate(name='concat')([user_embedding, item_embedding])
        x = tf.keras.layers.Dense(64, activation='relu', name='dense1')(concat)
        x = tf.keras.layers.Dropout(0.2, name='dropout1')(x)
        x = tf.keras.layers.Dense(32, activation='relu', name='dense2')(x)
        ncf_output = tf.keras.layers.Dense(1, activation='relu', name='ncf_output')(x)
        
        # Финальный выход: MF + NCF + biases
        output = tf.keras.layers.Add(name='final_add')([mf_output, ncf_output, user_bias, item_bias])
        
        model = tf.keras.Model(inputs=[user_input, item_input], outputs=output, name='CollaborativeFiltering')
        return model
    
    def compile_model(self):
        """Компиляция модели с MSE loss и MAE метрикой"""
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            loss='mse',
            metrics=['mae']
        )
    
    def train(self, user_ids, item_ids, ratings, epochs=10, batch_size=256, validation_split=0.1):
        """Обучение модели"""
        # Нормализация рейтингов в [0,1]
        ratings_min, ratings_max = ratings.min(), ratings.max()
        ratings_norm = (ratings - ratings_min) / (ratings_max - ratings_min)
        
        # Сохранение параметров для денормализации
        self.ratings_min = ratings_min
        self.ratings_max = ratings_max
        
        # Обучение с валидацией
        history = self.model.fit(
            [user_ids, item_ids], ratings_norm,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=1
        )
        return history
    
    def get_recommendations(self, user_id, num_recommendations=10, exclude_items=None):
        """Получение top-N рекомендаций для пользователя"""
        all_items = np.arange(self.num_items, dtype=np.int32)
        user_array = np.full(self.num_items, user_id, dtype=np.int32)
        
        # Предсказание рейтингов для всех items
        predictions = self.model.predict([user_array, all_items], verbose=0).flatten()
        
        # Исключение уже оцененных items
        if exclude_items is not None:
            predictions[exclude_items] = -np.inf
        
        # Top-N рекомендации
        top_indices = np.argsort(predictions)[-num_recommendations:][::-1]
        return top_indices
    
    def similarity_matrix(self, matrix_type='user'):
        """Вычисление матрицы сходства (cosine similarity)"""
        if matrix_type == 'user':
            embeddings = self.model.get_layer('user_emb').get_weights()[0]
        else:
            embeddings = self.model.get_layer('item_emb').get_weights()[0]
        
        similarity = cosine_similarity(embeddings)
        return similarity
    
    def user_based_recommendation(self, user_id, num_similar_users=10):
        """User-based collaborative filtering"""
        # Находим похожих пользователей
        similarity = self.similarity_matrix('user')
        similar_users = np.argsort(similarity[user_id])[::-1][1:num_similar_users+1]
        
        # Взвешенные рекомендации от похожих пользователей
        recommendations = {}
        for sim_user in similar_users:
            for item in range(self.num_items):
                if item not in recommendations:
                    recommendations[item] = []
                # Взвешенная оценка по сходству
                weight = similarity[user_id][sim_user]
                score = weight * 4.0 + np.random.random() * 0.5
                recommendations[item].append(score)
        
        # Агрегация оценок
        avg_scores = {k: np.mean(v) for k, v in recommendations.items()}
        top_items = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)[:10]
        return [item for item, _ in top_items]
    
    def item_based_recommendation(self, item_id, num_similar_items=10):
        """Item-based collaborative filtering"""
        similarity = self.similarity_matrix('item')
        similar_items = np.argsort(similarity[item_id])[::-1][1:num_similar_items+1]
        return similar_items
    
    def evaluate(self, user_ids, item_ids, ratings):
        """Оценка качества модели: MAE, RMSE"""
        predictions_norm = self.model.predict([user_ids, item_ids], verbose=0).flatten()
        
        # Денормализация предсказаний
        predictions = predictions_norm * (self.ratings_max - self.ratings_min) + self.ratings_min
        
        # Вычисление метрик
        mae = np.mean(np.abs(predictions - ratings))
        rmse = np.sqrt(np.mean((predictions - ratings)**2))
        
        print(f"MAE: {mae:.4f}")
        print(f"RMSE: {rmse:.4f}")
        return {'MAE': mae, 'RMSE': rmse}

# Генерация синтетических данных
def generate_sample_data(num_users=500, num_items=200):
    """Генерация синтетических данных рейтингов"""
    np.random.seed(42)
    n_samples = 10000
    
    user_ids = np.random.randint(0, num_users, n_samples)
    item_ids = np.random.randint(0, num_items, n_samples)
    
    # Симуляция предпочтений через латентные факторы
    true_user_prefs = np.random.normal(0, 0.5, (num_users, 8))
    true_item_prefs = np.random.normal(0, 0.5, (num_items, 8))
    
    ratings = np.sum(true_user_prefs[user_ids] * true_item_prefs[item_ids], axis=1)
    ratings = np.clip(ratings + np.random.normal(0, 0.3, n_samples), 1, 5)
    
    return user_ids.astype(np.int32), item_ids.astype(np.int32), ratings.astype(np.float32)

# ГЛАВНАЯ ПРОГРАММА
if __name__ == "__main__":
    print("Генерация данных...")
    user_ids, item_ids, ratings = generate_sample_data()
    
    print("Разделение данных на train/test...")
    train_users, test_users, train_items, test_items, train_ratings, test_ratings = \
        train_test_split(user_ids, item_ids, ratings, test_size=0.2, random_state=42)
    
    print("Инициализация модели...")
    cf = CollaborativeFiltering(num_users=500, num_items=200, embedding_dim=16)
    cf.compile_model()
    
    print("\nОбучение модели...")
    history = cf.train(train_users, train_items, train_ratings, epochs=10, batch_size=128)
    
    print("\nОценка модели:")
    metrics = cf.evaluate(test_users, test_items, test_ratings)
    
    print("\nTop-5 рекомендаций для пользователя 42:")
    recs = cf.get_recommendations(42, num_recommendations=5)
    print(recs.tolist())
    
    print("\nUser-based рекомендации для пользователя 42:")
    user_recs = cf.user_based_recommendation(42, num_similar_users=5)
    print(user_recs[:5])
    
    print("\nItem-based рекомендации для товара 10:")
    item_recs = cf.item_based_recommendation(10, num_similar_items=5)
    print(item_recs.tolist())
    
    # ВИЗУАЛИЗАЦИЯ (3 графика)
    plt.figure(figsize=(15, 5))
    
    # График 1: Динамика обучения
    plt.subplot(1, 3, 1)
    plt.plot(history.history['loss'], label='Train Loss', linewidth=2)
    plt.plot(history.history['val_loss'], label='Val Loss', linewidth=2)
    plt.title('Динамика обучения (MSE)', fontsize=12)
    plt.xlabel('Эпохи')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # График 2: Предсказания vs Истинные значения
    plt.subplot(1, 3, 2)
    test_preds_norm = cf.model.predict([test_users[:500], test_items[:500]], verbose=0).flatten()
    test_preds = test_preds_norm * (test_ratings[:500].max() - test_ratings[:500].min()) + test_ratings[:500].min()
    plt.scatter(test_ratings[:500], test_preds, alpha=0.7, s=20)
    plt.plot([1, 5], [1, 5], 'r--', linewidth=2, label='Ideal')
    plt.title(f'Предсказания\nMAE: {metrics["MAE"]:.3f}', fontsize=12)
    plt.xlabel('Истинные')
    plt.ylabel('Предсказанные')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # График 3: Top-10 рекомендаций
    plt.subplot(1, 3, 3)
    rec_scores = cf.model.predict([np.full(50, 42, dtype=np.int32), 
                                  np.arange(50, dtype=np.int32)], verbose=0).flatten()
    top10 = np.sort(rec_scores)[-10:]
    plt.bar(range(10), top10, color='orange')
    plt.title('Top-10 рекомендаций\nдля user=42', fontsize=12)
    plt.xlabel('Ранг')
    plt.ylabel('Предсказанный рейтинг')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cf_results.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("\nРезультаты сохранены: cf_results.png")
    print(f"Финальные метрики: MAE={metrics['MAE']:.4f}, RMSE={metrics['RMSE']:.4f}")
    
    # Архитектура модели
    print("\nАрхитектура модели:")
    cf.model.summary()
