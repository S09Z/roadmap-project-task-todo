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

## How to Run

### 1. Clone and Setup the Project

Follow the steps below to get the project up and running on your machine.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/<your-username>/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. **Create a virtual environment (optional but recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required dependencies** (if any, but in this case, the project doesn't have external dependencies).

### 2. Run the Following Commands

Once the project is cloned and the environment is set up, you can start using the CLI to manage tasks. Below are the commands:

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

1. Install `pytest` if you haven't already:

    ```bash
    pip install pytest
    ```

2. Run the tests:

    ```bash
    pytest
    ```

This will execute all test cases and verify that the application behaves as expected.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
