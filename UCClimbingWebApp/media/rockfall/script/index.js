const canvas = document.getElementById('game_area');
const context = canvas.getContext('2d');
context.font = "20px Arial";

let x = 100;
let y = 100;

const CLIMBER_WIDTH = 50; 
const CLIMBER_HEIGHT = 100;

const ROCK_WIDTH = 25;

const CANVAS_WIDTH = 800;
const CANVAS_HEIGHT = 600;

const DOWN_KEY_CODE = 40;
const UP_KEY_CODE = 38;
const LEFT_KEY_CODE = 37;
const RIGHT_KEY_CODE = 39;

let moveSpeed = 2;
let rockSpeed = 1;
let rockwallSpeed = 0.5;

const cursor = createCursor();

count = 0

let downPressed = false;
let upPressed = false;
let leftPressed = false;
let rightPressed = false;

let score = 0;

let score_sent = false;

const rocks = [];

const imgClimber = new Image();
imgClimber.onload = function () {
    drawGame();
}

imgClimber.src = imageClimber;

const imgRock = new Image();
imgRock.onload = function () {
    drawGame();
}

imgRock.src = imageRock;

const imgRockwall = new Image();
imgRockwall.onload = function () {
    drawGame();
}

imgRockwall.src = imageRockwall;

const rockwall = {
    x: 0,
    y: -800,
    flip: false
}

function drawGame() {
    if (!gameEnded){
        requestAnimationFrame(drawGame);
        clearScreen();
        spawnRocks();
        inputs();
        moveRocks();
        scrollRockwall();
        boundaryCheck();
        boundaryCheckRock();
        rockwallBoundaryCheck();
        drawRockwall();
        drawClimber();
        drawRocks();
        drawPlayerInfo();
        incrementScore();
        count += 1;
    }
    else {
        updateScoreInServer(score);
        requestAnimationFrame(drawGame);
        showGameOverScreen();
    }
}

// Game Over Screen to show the player what score they have and allow them to play again
function showGameOverScreen() {
    clearScreen();
    drawGameOverText();
    drawCursor();
    gameOverInputs();
}

function drawCursor() {
    
    if (cursor.cursorTop) {
        cursor.x = 280;
        cursor.y = 340;
    }
    else {
        cursor.x = 210;
        cursor.y = 390;
    }
    cursor.draw();
    return cursor
}

// Draws the text to the game over screen
function drawGameOverText() {
    const gameOverText = "GAME OVER";
    const gameOverTextObj = createCenteredTextObject(gameOverText, 60, 100);
    gameOverTextObj.draw();

    const playerText = "Player: " + username;
    const playerTextObj = createCenteredTextObject(playerText, 30, 200);
    playerTextObj.draw();
    
    const scoreText = "Score: " + score;
    const scoreTextObj = createCenteredTextObject(scoreText, 30, 250);
    scoreTextObj.draw();

    const playAgainText = "PLAY AGAIN"
    const playAgainTextObj = createCenteredTextObject(playAgainText, 30, 350);
    playAgainTextObj.draw();

    const leaderBoardText = "VIEW LEADER BOARD"
    const leaderBoardTextObj = createCenteredTextObject(leaderBoardText, 30, 400);
    leaderBoardTextObj.draw();



}

function createCursor() {
    const x_pos = 300;
    const y_pos = 340;
    const width = 15;
    const height = 15;
    const cursorTop = true;
    
    return {
        x: x_pos,
        y: y_pos,
        width: width,
        height: height,
        cursorTop: cursorTop,
        draw: function () {
            context.fillStyle = "white";
            context.fillRect(this.x, this.y, this.width, this.height);
        }

    }
}

// Creates a text object that automatically centers itself based on length
function createCenteredTextObject(text, fontSize, y) {
    const textWidth = context.measureText(text).width;
    const x_pos = (canvas.width/2) - (textWidth/2);
    const y_pos = y;

    return {
        text: text,
        x: x_pos,
        y: y_pos,
        draw: function() {
            context.fillStyle = "white";
            context.font = fontSize + "px Arial";
            context.textAlign = "center";
            context.textBaseline = "middle";
            context.fillText(this.text, canvas.width/2, y);
        }
    };
}

function incrementScore() {
    if (count % 50 === 0) {
        score += 5;
        if (score === 50) {
            gameEnded = true;
        }
    }
}

function boundaryCheck() {
    if (y < 0) {
        y = 0;
    }
    if (y > canvas.height - CLIMBER_HEIGHT) {
        y = canvas.height - CLIMBER_HEIGHT;
    }
    if (x < 0) {
        x = 0;
    }
    if (x > canvas.width - CLIMBER_WIDTH) {
        x = canvas.width - CLIMBER_WIDTH;
    }
}

function drawClimber() {
    context.drawImage(imgClimber, x, y);
}

function clearScreen() {
    context.fillStyle = "black";
    context.fillRect(0, 0, canvas.width, canvas.height);
}

function inputs() {
    if (upPressed) {
        y -= moveSpeed;
    }
    if (downPressed) {
        y += moveSpeed;
    }
    if (rightPressed) {
        x += moveSpeed;
    }
    if (leftPressed) {
        x -= moveSpeed;
    }
}

function gameOverInputs() {
    if (downPressed && cursor.cursorTop) {
        cursor.cursorTop = false;
    }
    if (upPressed && !cursor.cursorTop) {
        cursor.cursorTop = true;
    }
}

function spawnRocks() {
    if (count % 100 === 0) {
        var rock = {
            x: getRandomInt(0, canvas.width - ROCK_WIDTH),
            y: 0
        };
        rocks.push(rock);
    }
}

function drawRocks() {
    for (let i = 0; i < rocks.length; i++){
        context.drawImage(imgRock, rocks[i].x, rocks[i].y);
    }
}

function drawPlayerInfo() {
    context.fillText("Player: " + username, 0, 20);
    context.fillText("Score: " + score, 600, 20);
}

function moveRocks() {
    for (let i = 0; i < rocks.length; i++){
        rocks[i].y += rockSpeed;
    }
}

function boundaryCheckRock() {
    for (let i = rocks.length - 1; i >= 0; i--) {
        if (rocks[i].y > canvas.height) {
            rocks.splice(i, 1);
        }
    }
}

function drawRockwall() {
    context.drawImage(imgRockwall, rockwall.x, rockwall.y);
}

function scrollRockwall() {
    rockwall.y += rockwallSpeed;
}

function rockwallBoundaryCheck() {
    if (rockwall.y == 0) {
        rockwall.y = -800;
    }
}

document.body.addEventListener('keydown', keyDown);
document.body.addEventListener('keyup', keyUp)

function keyDown(event) {
    if (event.keyCode == UP_KEY_CODE) {
        upPressed = true;
    }
    if (event.keyCode == DOWN_KEY_CODE) {
        downPressed = true;
    }
    if (event.keyCode == LEFT_KEY_CODE) {
        leftPressed = true;
    }
    if (event.keyCode == RIGHT_KEY_CODE) {
        rightPressed = true;
    }
}

function keyUp(event) {
    if (event.keyCode == UP_KEY_CODE) {
        upPressed = false;
    }
    if (event.keyCode == DOWN_KEY_CODE) {
        downPressed = false;
    }
    if (event.keyCode == LEFT_KEY_CODE) {
        leftPressed = false;
    }
    if (event.keyCode == RIGHT_KEY_CODE) {
        rightPressed = false;
    }
}

function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}

function updateScoreInServer(score) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if (score_sent) return;

    $.ajax({
        type: 'POST',
        url: {% url "update_score" %},
        data: {
            "score": score,
            "csrfmiddlewaretoken": csrfToken
        },
        dataType: "json",
        success: function(data) {
            alert("Successfully delivered score");
            score_sent = true;
        },
        error: function(jqXHR, textStatus, errorThrown) {
            alert("Failed to deliver score: " + textStatus + " - " + errorThrown);
        }
    });
}