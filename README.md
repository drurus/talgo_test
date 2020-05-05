# talgo


Для запуска тестирования предварительно необходимо добавить данные:
    
   * в таблицу Activity (деятельность)
   * в таблицу Shop (товары)
   
---   

Копия БД снята командой:
   
    /usr/bin/pg_dump --host localhost --port 5432 --username "postgres" --role "talgo" --no-password  --format custom --blobs --encoding UTF8 --verbose --file "talgo_db.sql" "talgo_db"

Архив расположен в examples/talgo_db.tbz



    Написано в качестве тестового задания