const numberOfColumns =  3

function setup() {
    createCanvas(300, 300)
}

function draw() {
    background(205)
    //grid(3)
    rect(20, 23, 23, 23)
}

function mouseClicked(fxn)

function grid(numberOfColumns) {
    drawGrid = function(){
        stroke(0);
        strokeWeight(2)
        for (let i = 1; i < numberOfColumns; i++) {
            line(i * width / numberOfColumns, 0, i * width / numberOfColumns, height)
            line(0, i * height / numberOfColumns, width, i * height/numberOfColumns)
        }
    }
    drawGrid()
}

function drawNought(x, y) {
    noughtWidth = width / numberOfColumns
    push()
    strokeWeight(noughtWidth / 4)
    ellipse(x + noughtWidth / 2, y + noughtWidth / 2, noughtWidth/2, noughtWidth/2)
    pop()
}

function drawCross(x, y) {
    crossWidth = width / numberOfColumns
    push()
    strokeWeight(crossWidth / 4)
    strokeCap(SQUARE)
    fill(0,0, 0, 0.1)
    offset = 0.2
    line (
        x + crossWidth * offset,
        y + crossWidth * offset , 
        x + crossWidth * (1-offset), 
        y + crossWidth * (1 - offset)
    )
    line (
        x + crossWidth * (1-offset), 
        y + crossWidth * offset, 
        x + crossWidth * offset, 
        y + crossWidth * (1-offset)
    )
    pop()
}

