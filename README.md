# GitIssueCreator

GitIssueCreator is a Python tool designed to automate the creation of GitHub issues from a JSON file. It streamlines the issue tracking process for larger projects, ensuring that tasks are systematically logged and tracked in GitHub repositories.

## Features

-   Load tasks from a JSON file.
-   Automatically create GitHub issues for each task.
-   Environment variable integration for secure token handling.
-   Error handling for reliable issue creation.

## Getting Started

### Prerequisites

-   Python 3.x
-   `requests` library
-   `python-dotenv` library for environment variable management

### Installation

1. Clone the repository:
    ```bash
     git clone git@github.com:irvingzamora28/git-issue-creator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd git-issue-creator
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Installing Dependencies

Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

### Configuration

### Data File Setup

The script requires a JSON file (`data.json`) containing the issues to be created. Follow these steps to set it up:

1. Copy `data.example.json` to create your own `data.json` file:
   &&&bash
   cp data.example.json data.json
   &&&
2. Edit `data.json` and add your issue details according to the template format.

### .env File Setup

1. Create a `.env` file in the project root.
2. Add the following lines to the `.env` file:
    ```env
    GITHUB_TOKEN=your_github_token
    GITHUB_REPO=username/repo
    ```
3. Replace `your_github_token` with your personal GitHub token and `username/repo` with your GitHub repository details.

### Usage

Run the script with:

```bash
python main.py
```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Apache License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/your-username/git-issue-creator](https://github.com/your-username/git-issue-creator)
