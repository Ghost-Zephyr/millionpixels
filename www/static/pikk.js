
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

var reloadPikk = function() { // TODO: FIX, function only draws last for round
  let reqarr = []
  for (var i = 0; i < 1000; i++) {
    reqarr[i] = new XMLHttpRequest()
    reqarr[i].addEventListener('load', draw)
  }
  for (var i = 0; i < reqarr.length; i++) {
    reqarr[i].open('GET', `/pikk/${i}`)
    reqarr[i].send()
  }
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
