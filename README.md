## Description
# Truffle_suite_Ganache
A smart contract using Truffle suite to find the Reverse of a number. In the backed we have Ganache and connected front end and backend with python. 

## Steps
1. Create a new folder and run the command truffle init. 
2. Now change the directory by command cd and open the desired folder.
3. Open Ganache and add the project from contract and press save and restart button.
4. Now, inside that folder, open truffle-config.js file and uncomment development part and change the port number from 
ganache port and also change the version of compiler to 0.8.19.
5. Now open vscode and run the command on terminal- truffle create contract Reverse.
6. Inside contracts, we will get Reverse.sol file, and then we write the code for reverse of a number.
7. Now inside migrations folder, create one file 1_deploy.js write the code.
8. Now open the terminal and write truffle migrate.
9. Open Ganache and we have our project deployed successfully.
10. Create one foler src inside our project.
11. Move inside src folder and create one html file index.html for frontend.
12. For backend make one file test.py and write the code to connect with blockchain.
13. Create one more python file named app.py and import flask, and test.py and then connect index.html. Then call the reverse function inside this python file.
14. Now open index.html and run with a live server.
15. Enter any value and get the reverse of that number.


## Screenshot

![Screenshot 2024-03-19 162623](https://github.com/v3rma9579/Truffle_suite_Ganache/assets/79013592/9c811184-a181-477e-9541-2c7bbb0ad9c5)





![Screenshot 2024-03-19 160256](https://github.com/v3rma9579/Truffle_suite_Ganache/assets/79013592/60dc78e8-0df1-431f-a222-869033aeb8c7)




