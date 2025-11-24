const prompt = require("prompt-sync")();

function printSection(title) {
  console.log("==============================");
  if (title) console.log(title);
  console.log("==============================");
}

class TTTGame {
  constructor() {
    this.scoreboard;
    this.human = new Human();
    this.computer = new Computer();
  }

  static instructions() {
    console.log("Welcome to Tic Tac Toe! First to win 3 rounds wins.");
  }

  updateScoreboard(winner) {
    this.scoreboard[winner] = (this.scoreboard[winner] || 0) + 1;
  }

  setScoreboard(humanName) {
    this.scoreboard = {
      [humanName]: 0,
      "Computer": 0,
    }
  }

  play() {
    TTTGame.instructions();

    const humanName = this.human.getName();
    this.setScoreboard(humanName);

    this.human.chooseMarker();

    const humanMarker = this.human.getMarker();
    this.computer.setMarker(humanMarker === 'X' ? 'O' : 'X');

    while (true) {
      const round = new Round(this.human, this.computer);
      const winnerName = round.play();

      if (winnerName !== "Tie") {
        this.updateScoreboard(winnerName);
      }

      console.log("");
      console.log("Scoreboard: ", this.scoreboard);
      console.log("");

      for (let player in this.scoreboard) {
        if (this.scoreboard[player] >= 3) {
          console.log(`${player} wins the match!`);
          return;
        }
      }
      
    }

  }
}

class Round {
  constructor(human, computer) {
    this.human = human;
    this.computer = computer;
    this.board = new Board();
    this.currentPlayer = this.chooseFirstPlayer(this.human, this.computer);

  }

  chooseFirstPlayer(player1, player2) {
    const randomNum = Math.floor(Math.random() * 2);
    return randomNum === 0 ? player1 : player2;
  }

  play() {
    printSection("Starting new round!");
    this.board.displayBoard();

    while (true) {
      let move = this.currentPlayer.getMove(this.board);
      if (!/^[1-9]$/.test(move)) return false;
      
      while (!this.board.isSquareAvailable(move)) {
        console.log("Unavailable square.");
        move = this.currentPlayer.getMove(this.board);
      }
      
      this.board.markBoard(this.currentPlayer.getMarker(), move);

      printSection(`${this.currentPlayer.name} picked ${move}`);
      this.board.displayBoard();

      const winner = this.board.checkForWinner();
      if (winner) {
        console.clear();
        printSection(`${this.currentPlayer.name} wins this round!`);
        this.board.displayBoard();
        return this.currentPlayer.name;
      }

      if (this.board.isFull()) {
        console.clear();
        printSection("It's a tie for this round!");
        this.board.displayBoard();
        return "Tie";
      }

      this.switchPlayer();
    }
  }

  switchPlayer() {
    if (this.currentPlayer instanceof Human) {
      this.currentPlayer = this.computer;
    } else {
      this.currentPlayer = this.human;
    }
  }

}

class Board {
  static positionMap = {
      '1': [0, 0], '2': [0, 1], '3': [0, 2],
      '4': [1, 0], '5': [1, 1], '6': [1, 2],
      '7': [2, 0], '8': [2, 1], '9': [2, 2], 
  }

  static WINNING_COMBOS = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
    ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
    ['1', '5', '9'], ['3', '5', '7']
  ]

  constructor() {
    this.board = [
      ['1', '2', '3'], 
      ['4', '5', '6'], 
      ['7', '8', '9']];

  }

  displayBoard() {
    console.log(` ${this.board[0][0]} | ${this.board[0][1]} | ${this.board[0][2]}`);
    console.log("-----------");
    console.log(` ${this.board[1][0]} | ${this.board[1][1]} | ${this.board[1][2]}`);
    console.log("-----------");
    console.log(` ${this.board[2][0]} | ${this.board[2][1]} | ${this.board[2][2]}`);
  }

  markBoard(marker, position) {
    const [row, col] = Board.positionMap[position];
    this.board[row][col] = marker;
  }

  isSquareAvailable(position) {
    const coordinates = Board.positionMap[position];
    if (!coordinates) return false;

    const [row, col] = coordinates;
    return this.board[row][col] === position;
  }

  isFull() {
    return this.board.flat().every(cell => cell === 'X' || cell === 'O');
  }

  getAvailableSquares() {
    const availableSquares = this.board.flat().filter(square => square !== 'X' && square !== 'O');
    return availableSquares;
  }

  checkForWinner() {
    for (let combo of Board.WINNING_COMBOS) {
      const [pos1, pos2, pos3] = combo;
      const [r1, c1] = Board.positionMap[pos1];
      const [r2, c2] = Board.positionMap[pos2];
      const [r3, c3] = Board.positionMap[pos3];

      const marker1 = this.board[r1][c1];
      const marker2 = this.board[r2][c2];
      const marker3 = this.board[r3][c3];
        
      if (marker1 === marker2 && marker2 === marker3) {
        return marker1;
      }
    }
    return null;
  }
}

class Player {
  constructor() {
    this.marker = null;
  }

  getMarker() {
    return this.marker;
  }

  static validateMarker(marker) {
    return marker === 'X' || marker === 'O';
  }

}

class Human extends Player {
  constructor() {
    super();
    this.name;
  }

  getName() {  
    const name = prompt("What is your name? ");
    this.name = name;
    return this.name;
  }

  chooseMarker() {
    let marker;

    do {
      marker = prompt("Choose X or O: ").toUpperCase();
    } while (!Player.validateMarker(marker)) 

    this.marker = marker;
  }

  getMove() {
    let position = prompt("Pick a square (1-9): ").trim();
    return position;
  }
}

class Computer extends Player{
  constructor() {
    super();
    this.name = "Computer";
  }
  
  setMarker(marker) {
    this.marker = marker;
  }

  getMove(board) {
    const winningMove = this.findSinglePlay(board, this.marker);
    if (winningMove) return winningMove;

    const humanMarker = this.marker === 'X' ? 'O': 'X';
    const blockingMove = this.findSinglePlay(board, humanMarker);
    if (blockingMove) return blockingMove;

    if (this.isCenterOpen(board)) return "5";

    const choices = board.getAvailableSquares();
    return choices[Math.floor(Math.random() * choices.length)];
  }

  findSinglePlay(board, marker) {
    for (let combo of Board.WINNING_COMBOS) {

      const markedSquares = combo.filter(square => {
        const [row, col] = Board.positionMap[square];
        return board.board[row][col] === marker;
      });

      if (markedSquares.length === 2) {

        const emptySquare = combo.find(square => {
          const [row, col] = Board.positionMap[square];
          const value = board.board[row][col];
          return value !== 'X' && value !== 'O';
        });
        
        if (emptySquare) return emptySquare;
      }
    }
    return null;
  }

  isCenterOpen(board) {
    const [row, col] = Board.positionMap["5"];
    const value = board.board[row][col];
    return value !== "X" && value !== "O";

  }
}

let game = new TTTGame();
game.play();