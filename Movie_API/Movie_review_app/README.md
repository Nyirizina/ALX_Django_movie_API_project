Week 1 Documentation:
- Organized the libraries of the project.
- Created Movie_review_app for the Movie_API project and added the app in the project settings.
- Created New models for the movie review app which are Movie model, Rating model, Review model.
- Created a path for the Movie_review_app/urls.py in the Movie_API/urls.
- Created a mysql_database and connected the database ('Movie_review') with the Movie_review_app.

Week 2 documentation:
- In week 2 we have added a User model to help with allowing users to use there username, email, password to access the movie_review_api.
- We created a Serializer to help in changing the format of our models to normal json file that can be readable.
- We added a rest_framework app to help in building web APIs.

Week 3 documentation:
- We were able to modify the models and remove unnessesary models created in the above tasks and remained with the appropriate model.
- Created viewsets for the model that was created and added a queryset to access all data in the database.
- Next steps we are going to work on authentication, permissions and setting up urls for the user to access our API.

Week 4 documentation:
- Added permissions so that a user can only update or delete their own views.
- In views we called our previously created permissions so that a user  can be able to  update or delete their own views, and also we have a modelviewset that will help in logic of all CRUD operations
- finally we added a Default router that will help to automatically generate necessary RESTful routes.

Week 5 documentation:
- after creating our app we added filtering to help a user on being able to search or order their reviews based on rating, movie_title, content.
- In the last week we were able to finalize our project and now our user can manage reviews for movies by adding, updating, deleting, and viewing reviews.