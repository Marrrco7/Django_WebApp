
Overview
--------

This project is a dynamic web application developed using Django, allowing for easy addition, update, display, and deletion of game information. The application integrates with a PostgreSQL database to efficiently store and retrieve game data.

Table of Contents
-----------------

- Project Structure
- Features
- Analysis and Design
  - Challenge Overview
  - Solution Architecture
  - Functional Requirements
  - Non-Functional Requirements
  - System Architecture
  - Database Design

Project Structure
-----------------




Features
--------

- **CRUD Operations**: Create, Read, Update, and Delete video game entries.
- **User Authentication**: Secure login and logout functionalities.
- **Permissions**: Restrict access to certain views based on user permissions.
- **Responsive Design**: User interface built with Bootstrap for responsiveness.


Analysis and Design
-------------------

### Solution Architecture

The architecture consists of the following components:

- **Functional Web Application**: A Django web application that allows management of a video game catalog with CRUD functionalities. It defines a `VideoGame` model to represent each video game, including fields for the game's title, genre, release date, and a brief description.
- **Database Integration**: Integration with a PostgreSQL database, ensuring efficient data storage and retrieval for game information.

### Functional Requirements

- **Add New Game**: Users can add new video games by specifying the title, genre, release date, and a brief description.
- **Edit Game Details**: Users can update existing game information.
- **Delete Game**: Users can remove games from the catalog.
- **View Game List**: Users can view a list of all games in the catalog.
- **User Authentication**: Users must log in to access the application.
- **Permissions**: Only authorized users can add, edit, or delete games.

### Non-Functional Requirements

- **Performance**: The application should load pages within 2 seconds.
- **Scalability**: The system should handle up to 100 concurrent users.
- **Security**: Implement proper authentication and authorization mechanisms.
- **Usability**: The interface should be intuitive and easy to navigate.
- **Maintainability**: Code should follow best practices for readability and maintainability.

### System Architecture

The application follows the Model-View-Template (MVT) architectural pattern provided by Django.

- **Models**: Define the structure of the database (VideoGame and Genre models).
- **Views**: Handle the business logic and interact with the models.
- **Templates**: Render the user interface using HTML and Bootstrap.

### Database Design

A PostgreSQL database is used to store game information.

**Tables**:

1. **Genre**
   - `id`: Primary key
   - `title`: String (max 50 characters)

2. **VideoGame**
   - `id`: Primary key
   - `title`: String (max 100 characters)
   - `release_date`: Date
   - `description`: String (max 100 characters)
   - `genre_id`: Foreign key referencing `Genre`

### User Interface Design
 **Base Template**: Includes navigation and common UI elements.
- **Videogame List**: Displays a table of all video games with options to edit or delete.
- **Videogame Form**: Form for adding or editing a video game.
- **Authentication Pages**: Login and logout pages.

**Design Elements**:

- **Bootstrap 4.3.1**: Used for responsive design and styling (includes the jumbotron component).
- **Font Awesome 6.6.0**: Provides icons for buttons and actions.
- **Jumbotron Component**: Used for the header section in the base template.
- **Base Template**: Includes navigation and common UI elements.
- **Videogame List**: Displays a table of all video games with options to edit or delete.
- **Videogame Form**: Form for adding, deleting or updating videogames
