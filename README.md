# Мой Проект с gRPC, GraphQL и Worker

**Описание:**
Это многокомпонентное приложение, объединяющее в себе:
* **gRPC сервис:** Обеспечивает работу с elasticsearch и быструю передачу данных.
* **GraphQL сервис:** Предоставляет собой интерфейс для взаймодействия с gRPC сервисом.
* **Worker:** Выполняет простой парсинг JSON данных из файла и отправляет в gRPC сервис.

**Установка:**
1. **Клонирование репозитория:**
   ```bash
      git clone [URL]
   ```

2. **Установка зависимостей:**
    ```bash
      cd my-project
      python -m venv .venv && source .venv/bin/activate
      pip install -r requirements.txt 
    ```
3. **Запуск:**
   ```bash
      gRPC python -m app.servers.grpc 
      GraphQL python -m app.servers.graphql 
      Worker python -m workers.parser (Не докерезирован!!!)
      Docker docker compose up -d
    
      Для запуска gRPC, GraphQL, Worker пример:
        GRPC_CLIENT_ADS_HOST=localhost GRPC_CLIENT_ADS_PORT=51600 python -m workers.parser
    ```

4. **Переменные и команда запуска**
* **Worker:**
* ***command:*** python -m worker.parser
  - GRPC_CLIENT_ADS_HOST    
    - **default**: localhost 
    - **data_type**: string
  - GRPC_CLIENT_ADS_PORT
    - **default**: 50050 
    - **data_type**: int

* **gRPC:**
* ***command:*** python -m app.servers.grpc
  - SERVICE_GRPC_HOST    
    - **default**: [::] 
    - **data_type**: string
  - SERVICE_GRPC_PORT
    - **default**: 51600 
    - **data_type**: int
  - SERVICE_GRPC_DB_ELASTICSEARCH_SCHEMA    
    - **default**: http 
    - **data_type**: string
  - SERVICE_GRPC_DB_ELASTICSEARCH_HOST
    - **default**: localhost 
    - **data_type**: string
  - SERVICE_GRPC_DB_ELASTICSEARCH_PORT
    - **default**: 9200 
    - **data_type**: int

* **GraphQL:**
* ***command:*** python -m app.servers.graphql
  - SERVICE_GRAPHQL_HOST    
    - **default**: 0.0.0.0 
    - **data_type**: string
  - SERVICE_GRAPHQL_PORT
    - **default**: 8000 
    - **data_type**: int
  - GRPC_CLIENT_ADS_HOST    
    - **default**: localhost
    - **data_type**: string
  - GRPC_CLIENT_ADS_PORT
    - **default**: 51600
    - **data_type**: int
