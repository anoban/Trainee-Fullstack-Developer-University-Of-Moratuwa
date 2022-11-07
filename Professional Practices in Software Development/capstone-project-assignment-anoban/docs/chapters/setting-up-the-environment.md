## 1. Setting up the environment

- Before starting to implement the `Student Management System`, we need to set up the required environment for the project. Below sections will guide you to set up the environment. If you have already installed them, you can skip the relevant sections.

### 1.1. Installing Node.js

Check whether `Node.js` and `npm package manager` is already installed by typing the following commands in the command line.
```bash
# Check the Node.js version
node -v

# Check the npm version
npm -v
```

> **Important**: This project requires a Node.js version of 14 or higher.

If the above is not installed, download suitable `Node.js` package for your OS using the following [link](https://nodejs.org/en/download/) and install it.

> For a guided `Node.js` installation, refer to [4.3 Setup Angular Environment](https://open.uom.lk/mod/hvp/view.php?id=715) in the **Course 4 - Front-End Web Development**

### 1.2. Installing Angular

Check whether `Angular CLI` is already installed by typing the following command in the command line.
```bash
# Check whether Angular CLI is available 
ng
```

If the `Angular CLI` is not installed, install it using the `npm package manager` by typing the following command in the command line.
```bash
# Install Angular CLI globally
npm install -g @angular/cli
```

### 1.3. Installing Dependencies

After completing the above installations, we must install the dependencies specified in the `package.json` files for the `backend` and the `frontend`.

- To install the dependencies of the backend, type the following command from the root of the project.
```bash
# Install the dependencies
npm install
```

- To install the dependencies of the frontend, first navigate to the frontend folder and then install the dependencies using the following command.
```bash
# Navigate to frontend directory
cd frontend

# Install the dependencies
npm install
```

### 1.4. Database Migration and Seeding

In order to create the necessary `tables` and insert the `dummy data` for the tables we need to run the following command.

We do this in two steps.

1. The first step is to migrate the database which creates the tables in the database.

```bash
npm run migrate
```

2. The second step is to populate the created tables with dummy data (seed)

```bash
npm run seed
```

### 1.5. Installing Git

To maintain the Capstone Project code, we will be using a **distributed version control system** called `git`.

- To check whether you have already installed `git`, type the following command in a terminal.

```bash
git
```

- If the terminal doesn't understand the command, you need to install `git`. Use the given link to download `git` and then complete the installation process.

[Download from here](https://git-scm.com/downloads)