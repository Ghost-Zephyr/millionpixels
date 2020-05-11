
let ctx = document.getElementById('pikk').getContext('2d')
ctx.mozImageSmoothingEnabled = false
ctx.imageSmoothingEnabled = true

var draw = function() {
  let res = JSON.parse(this.responseText)
  for(var n in res) {
    pixel = res[n]
    ctx.fillStyle = pixel['color']
    ctx.fillRect(pixel['x'], pixel['y'], 1,1)
  }
}

var reloadPikk = function() {
  var req = new XMLHttpRequest()
  req.addEventListener('load', draw)
  req.open('GET', '/pikk')
  req.send()
}

reloadPikk()

/*

function draw() {
  console.log(this.responseText)
}

var req = new XMLHttpRequest()
req.addEventListener('load', draw)
req.open('GET', '/pikk')
req.send()

*/

