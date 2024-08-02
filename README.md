### Summary



### Résumé de l'histoire

L'histoire commence dans une forêt sombre et mystérieuse, où le protagoniste se trouve face à un choix crucial : aller à gauche ou à droite. À chaque décision, l'aventure prend un tournant inattendu. En choisissant d'aller à gauche, le protagoniste rencontre un loup féroce, forçant le joueur à décider entre combattre ou fuir. Aller à droite, en revanche, mène à la découverte d'une carte au trésor, offrant la possibilité de suivre la carte ou de l'ignorer.

Au fur et à mesure que l'histoire progresse, chaque choix plonge le protagoniste dans des situations plus dangereuses ou plus agréables. L'objectif ultime est d'atteindre une fin héroïque, que ce soit en explorant un temple ancien, en découvrant des trésors cachés, ou en s'échappant de la forêt. Le joueur doit naviguer à travers ces choix, pesant les risques et les récompenses, pour mener le protagoniste à la gloire ou à la sécurité.



This project is an interactive story game built using Flask, HTML, and CSS. The game allows users to navigate through a story by making choices at various decision points. Each choice leads to a different part of the story, with unique images and background colors that reflect the mood of each situation (e.g., danger or pleasure). The goal is to reach a heroic ending by making the right decisions throughout the game.

### README

#### Project Title: Interactive Story Game

#### Description

An interactive story game where users navigate through a story by making choices at various decision points. Each decision affects the outcome of the story, leading to different paths and endings. The game features dynamic background colors and images to enhance the storytelling experience.

#### Features

- Interactive story with multiple paths and endings
- Dynamic background colors based on the mood of the situation
- Unique images for each part of the story
- Simple and intuitive interface

#### Technologies Used

- Flask (Python)
- HTML
- CSS
- JSON

#### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/interactive-story-game.git
   cd interactive-story-game
   ```
2. **Create a virtual environment:**

   ```sh
   python3 -m venv venv
   ```
3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. **Install the dependencies:**

   ```sh
   pip install Flask
   ```

#### Usage

1. **Run the Flask app:**

   ```sh
   python app.py
   ```
2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```
3. **Start the interactive story by making your choices and exploring different paths.**

#### Project Structure

```
project/
│
├── app.py                      # Flask application
├── data/
│   └── nodes.json              # JSON file containing story nodes
├── static/
│   ├── css/
│   │   └── styles.css          # CSS styles
│   └── images/                 # Folder containing story images
│       ├── forest.jpg
│       ├── wolf.jpg
│       ├── treasure_map.jpg
│       ├── secret_passage.jpg
│       ├── lost_forest.jpg
│       ├── treasure.jpg
│       ├── forest_exit.jpg
│       ├── temple.jpg
│       ├── forest_path.jpg
│       ├── rescue.jpg
│       ├── wealth.jpg
│       ├── safe_exit.jpg
│       └── hero.jpg
└── templates/
    └── index.html              # HTML template for the story
```

#### Customization

To customize the story or add new paths, update the `nodes.json` file in the `data` directory. Each node in the JSON file represents a part of the story and includes the text, image, choices, and background color.

Example node structure in `nodes.json`:

```json
{
    "node_key": {
        "text": "Story text here.",
        "image": "images/your_image.jpg",
        "choices": {
            "Choice 1 text": "next_node_key",
            "Choice 2 text": "another_node_key"
        },
        "color": "#FFFFFF"  // Background color for this node
    }
}
```

#### License

This project is licensed under the MIT License.

#### Contact

For any questions or suggestions, please contact ISSA IBRAHIM Moubarak at 2im.moubarak@gmail.com.
