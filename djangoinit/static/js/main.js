navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
    console.log(stream)
}).catch((err) => console.log(err))