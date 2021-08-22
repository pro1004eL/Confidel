# Web-service "Confidel"
Создание собственного проекта в рамках курсов "Тестирование ПО" Вадима Ксендзова.

Цель проекта: углубленное понимание процессов того, как работает API, клиент-серверная архитектура, самостоятельное написание API документации в Swagger.

Требуется: придумать собственную систему, взаимодействующую с БД, написать требования для данной системы, user-story, accceptance criteria. 

Ход выполнения: Cоздание проекта для кондитерской фабрики "Confidel". После написания user-story и acceptance criteria для landing page "Confidel", я создал таблицы в БД PostgreSQL, задав необходимые связи и наполнив ее тестовыми данными. Далее ожидалось, что Вадим, согласно моим требованиям, реализует систему на языке Python. Однако, в ходе выполнения было принято решение, что реализовывать систему возьмусь я лично, тем самым ближе познакомившись с языком Python, и Swagger - инструмент для описания API. После успешной реализации система была протестирована с помощью Postman.

Проект включает в себя:

http://23.88.52.139:5002/swagger/  - реализация Swagger.

main_padawan.py - реализация API на языке python.

API_desc.txt - описание БД. 

User_story.txt - описание user-story системы и accceptance criteria.

Web_server.postman_collection.json - коллекция Postman с тестами API для реализованной системы.

Confidel_testing.mp4 - видео тестирования реализованной системы с помощью Postman, примеры запросов, ответов, изменений в БД.

confidel_WEB_Service_app_index.html.png - landing page кондитерской "Confidel".

