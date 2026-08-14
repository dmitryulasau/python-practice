function getComputerChoice() {
    let number = Math.random();
    if (number < 1 / 3) {
        return "rock";
    } else if (number < 2 / 3) {
        return "paper";
    } else {
        return "scissors";
    }
}

function getHumanChoice() {
    let choice = prompt("Choose rock, paper, or scissors:");
    if (choice === null) {
        return null;
    }
    return choice.toLowerCase();
}

let humanScore = 0;
let computerScore = 0;

function playRound(humanChoice, computerChoice) {
    if (humanChoice === computerChoice) {
        return "It's a tie!";
    }
    if (humanChoice === "rock" && computerChoice === "scissors") {
        humanScore++;
        return "You win! rock beats scissors";
    }
    if (humanChoice === "paper" && computerChoice === "rock") {
        humanScore++;
        return "You win! paper beats rock";
    }
    if (humanChoice === "scissors" && computerChoice === "paper") {
        humanScore++;
        return "You win! scissors beats paper";
    }
    computerScore++;
    return "You lose! " + computerChoice + " beats " + humanChoice;
}

function playGame() {
    for (let i = 0; i < 3; i++) {
        let humanChoice = getHumanChoice();
        if (humanChoice === null) {
            alert("Game cancelled :(");
            return;
        }
        let computerChoice = getComputerChoice();
        alert(playRound(humanChoice, computerChoice));
    }
    if (humanScore > computerScore) {
        alert("You win the game!");
    } else if (computerScore > humanScore) {
        alert("You lose the game! :(");
    } else {
        alert("It's a tie!");
    }
}

playGame();