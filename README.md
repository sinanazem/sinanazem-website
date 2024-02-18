# Sina Nazem - Personal Website
<img src="https://www.bootstrapdash.com/wp-content/uploads/2019/08/Personal-Portfolio-website-templates.png"><br>
## Overview

Welcome to the repository for my personal website, [sinanazem.com](https://sinanazem.com). This project is built using Django for the backend, JavaScript for interactivity, and Bootstrap for styling.

## Features

- **Portfolio:** Showcase your projects, achievements, and skills.
- **Blog:** Share your thoughts, experiences, and insights with a built-in blog.
- **Contact:** Allow visitors to get in touch with you through a contact form.

## Technologies Used

- **Django:** A high-level Python web framework for building web applications.
- **JavaScript:** Used for adding dynamic and interactive elements to the website.
- **Bootstrap:** A popular front-end framework for responsive and visually appealing designs.

## Getting Started

### Prerequisites

- Python 3.x
- Django (install using `pip install Django`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sinanazem/sinanazem-website.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sinanazem-website
    ```

3. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Visit `http://127.0.0.1:8000/` in your web browser.

## Usage

1. **Customization:**
   - Update the `portfolio`, `blog`, and `contact` sections in the Django admin panel.
   - Add your personal information and customize the site to fit your style.

2. **Development:**
   - Modify the templates in the `templates` directory to personalize the appearance.
   - Extend functionality by adding more views, models, or integrating additional JavaScript features.

## Deployment

- This project is ready for deployment to platforms like Heroku, AWS, or any other hosting service.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

- Special thanks to the Django, JavaScript, and Bootstrap communities for their excellent documentation and support.

---

Feel free to reach out if you have any questions or suggestions. Happy coding!
