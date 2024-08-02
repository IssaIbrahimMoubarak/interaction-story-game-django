
# Interactive Story Project

## Overview

This is an interactive story web application built with Django. The project allows users to make choices within a narrative, leading to different outcomes. The content dynamically updates based on user selections, creating an engaging experience.

## Features

- **Dynamic Story Navigation:** Users can progress through the story by making choices that direct them to different story nodes.
- **AJAX Integration:** Choices update the story content dynamically without requiring a full page reload.
- **Admin Interface:** Easily manage story nodes and choices using Django's built-in admin interface.
- **Customizable Appearance:** Each story node can have its own text, image, and background color.

## Project Structure

- `interactive_story/`: The main Django project directory.
  - `settings.py`: Configuration settings for the project.
  - `urls.py`: URL routing for the project.
- `story/`: The application handling the interactive story.
  - `models.py`: Defines the `StoryNode` and `Choice` models.
  - `views.py`: Handles the rendering of story nodes and processing user choices.
  - `urls.py`: URL routing specific to the story app.
  - `admin.py`: Registers the models with the Django admin interface.
  - `templates/story/home.html`: The HTML template for displaying the story and choices.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- A virtual environment is recommended for isolating dependencies.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/interactive-story.git
   cd interactive-story
   ```
2. **Set Up the Virtual Environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```
5. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```
6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```
7. **Access the Application:**

   Open your browser and go to `http://127.0.0.1:8000/`.
8. **Access the Admin Interface:**

   Go to `http://127.0.0.1:8000/admin/` to manage story nodes and choices.

### Usage

- Navigate through the story by making choices presented on the page.
- The URL updates to reflect the current story node, while the page content dynamically changes.

### Managing Content

1. **Add Story Nodes:**

   - Go to the Django admin interface.
   - Add new `StoryNode` objects with the required key, text, image, and color.
2. **Add Choices:**

   - After creating story nodes, add `Choice` objects that link nodes together.
3. **Test the Story:**

   - Visit the homepage and interact with the story to ensure the choices and story flow correctly.

### Customization

- **Templates:**
  - Modify `home.html` to change the layout or styling of the story pages.
- **Static Files:**
  - Add custom CSS or JavaScript files to enhance the user experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## Acknowledgements

- Django for providing an excellent framework for web development.
- The community for their helpful resources and tutorials.
