var aliens = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]];
var alienX = 10;
var alienY = 50;
var bulletX = 50;
var bulletY = 565;
var playerX = 250;
var bulletFired = false; 
var alienSpeedX = 1;
var alienXR = 610;
var alienXL = alienX;
var alienSpaceX = 60;
var alienSpaceY = 70;
var alienYcounter = 0 ;
var text = true;
var shipImage;
var pBulletImage;
var alienImage;
var myScore = 0;
var alienBulletX = 4;
var alienBulletY = 4; 
function setup() {
	createCanvas(700,600);
	background(0);
	shipImage = loadImage("Ship.png");
	ship = createSprite(playerX + 15, 575);
	ship.addImage("normal", shipImage);
	alienImage = loadImage("alien.png");
	//alien = createSprite();
	//alien.addImage("normal", alienImage);

}


function intersect(bulletX, bulletY, alienX, alienY) {
	if ((bulletX > alienX - 20) && (bulletX < alienX + 20) && (bulletY > alienY - 20) && (bulletY < alienY + 20)){
		return 1;
	}
	else {
		return 0;
	}
}




function draw() {
	background(0);
	rect(playerX, 565, 30, 30);
	textSize(32);
	fill(255);
	text("Score", 10, 30);
	text(myScore, 125, 30);


	alienX = alienX + alienSpeedX; // Boundaries!!!!
	alienXL = alienXL + alienSpeedX;
	alienXR = alienXR + alienSpeedX;

	//Counts the amount of time aliens hit walls and moves them down
	var shipImage;
	if ((alienXR > 700 - 15) || (alienXL < -40)){
		alienSpeedX = alienSpeedX * -1;
		alienYcounter = alienYcounter + 1;
	}
	//Counts the amount of time aliens hit walls and moves them down
	if ((alienYcounter % 5 == 0) && (alienYcounter != 0)){
		alienY = alienY + .1;
	}
	/*Draws the aliens */
	for (i = 1; i < aliens.length; i++){
		for (j = 1; j < aliens[i].length; j++){
			
			if (aliens[i][j] == 1) {
				ellipse(alienX + (i * alienSpaceX), alienY + (j * alienSpaceY), 30,30);
				image(alienImage, alienX - 20 + (i * alienSpaceX), alienY - 20 + (j * alienSpaceY));

				//alien(alienX + i * 50, alienY + j * 60);
			}

			if ( (aliens[i][j] == 1) && (intersect(bulletX, bulletY, alienX + i * alienSpaceX, alienY + j * alienSpaceY)) ){
				aliens[i][j] = 0;
				bulletFired = false;
				bulletY = 565;
				myScore = myScore + 10;
				print(myScore);

			}
		
		}
	}
	/*Player Moving Keys*/
	if (keyDown(LEFT_ARROW)== true) {
		playerX = playerX - 5;
		ship.position.x = playerX + 15;
	}
	if (keyDown(RIGHT_ARROW)== true) {
		playerX = playerX + 5;
		ship.position.x = playerX + 15;
	}

	if (keyDown(UP_ARROW)== true){
		if (bulletFired == false){
			bulletX = playerX + 15;
			bulletFired = true;
		}


	}

	if (bulletFired == true) { /*Players Bullet*/
		rect(bulletX - 5, bulletY, 5, 10);
		bulletY = bulletY - 10;
		
		if (bulletY < 0) {
			bulletFired = false;
			bulletY = 565;
		}
		
	}
	var row = 1
	var col = 1
	if (aliens[row][col] == 1){
		rect(alienBulletX, alienBulletY, 5, 10);
		alienBulletY = alienBulletY + 5;


	}
	//if (alienFired == true){
	//	rect()
	//}


	drawSprites();
	}

