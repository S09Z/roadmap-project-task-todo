# Task Tracker

This project is part of the **"Task Tracker" challenge from [roadmap.sh](https://roadmap.sh/projects/task-tracker)**, which helps users practice building CLI applications.

Task Tracker is a command-line interface (CLI) application that helps you manage your tasks efficiently. You can add, update, delete tasks, and mark them as in-progress or done. The tasks are stored in a JSON file, allowing for persistence across sessions.

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark tasks as in-progress or done
- List all tasks
- List tasks by status: done, todo, in-progress

## Requirements

- Python 3.6 or higher
- (Optional) [Poetry](https://python-poetry.org/) for dependency and environment management

## How to Run

### 1. Clone and Setup the Project

#### Option 1: Standard Python Virtual Environment Setup

Follow the steps below to get the project up and running on your machine.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/S09Z/roadmap-project-task-todo.git
    cd task-tracker-cli
    ```

2. **Create a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required dependencies** (if any, but in this case, the project doesn't have external dependencies).

#### Option 2: Using Poetry for Setup

Alternatively, you can use **Poetry** to manage the virtual environment and dependencies. Follow these steps:

1. **Install Poetry** (if not already installed):

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

    Or follow the installation guide from the official [Poetry documentation](https://python-poetry.org/docs/#installation).

2. **Clone the repository**:

    ```bash
    git clone https://github.com/<your-username>/task-tracker-cli.git
    cd task-tracker-cli
    ```

3. **Install dependencies and setup environment**:

    Poetry will automatically create a virtual environment for you and install the dependencies.

    ```bash
    poetry install
    ```

4. **Activate the virtual environment**:

    To use the environment Poetry created, you can activate it with:

    ```bash
    poetry shell
    ```

5. **Run the following commands** inside the Poetry shell (or using `poetry run`):

    Once the project is set up, you can start using the CLI to manage tasks.

    1. **Add a new task**:

        ```bash
        python task-cli.py add "Buy groceries"
        ```

    2. **Update a task**:

        ```bash
        python task-cli.py update 1 "Buy groceries and cook dinner"
        ```

    3. **Delete a task**:

        ```bash
        python task-cli.py delete 1
        ```

    4. **Mark a task as in progress**:

        ```bash
        python task-cli.py mark-in-progress 1
        ```

    5. **Mark a task as done**:

        ```bash
        python task-cli.py mark-done 1
        ```

    6. **List all tasks**:

        ```bash
        python task-cli.py list
        ```

    7. **List tasks by status**:

        - List done tasks:
          ```bash
          python task-cli.py list done
          ```

        - List tasks in progress:
          ```bash
          python task-cli.py list in-progress
          ```

        - List tasks to do:
          ```bash
          python task-cli.py list todo
          ```

## JSON Storage

All tasks are saved in a `tasks.json` file in the current directory. This file will be created automatically when you add your first task.

## Running Tests

The project includes automated tests written using `pytest`. To run the tests:

1. **If using Poetry**, run the tests inside the Poetry environment:

    ```bash
    poetry run pytest
    ```

2. **If using standard environment**, run the tests:

    ```bash
    pytest
    ```

This will execute all test cases and verify that the application behaves as expected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
