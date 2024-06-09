# Frontend Running Guide
1. install [Google Chrome](https://www.google.com/intl/en_au/chrome/) latest version
2. install Node and NPM [here](https://nodejs.org/en/download/) 
    - or via command line: `sudo apt update` and `sudo apt install nodejs` (for Linux)
3. install Yarn on Linux `sudo npm i -g yarn`
4. on terminal, navigate to project repository with `cd project`
5. on terminal, run `yarn install` to install packages (this step might take some time)
6. on terminal, run `yarn start` to run the frontend
    - Note: if this step failed, run `yarn upgrade` before `yarn start`
7. open Google Chrome and search `http://localhost:3000`