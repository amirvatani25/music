var updateBtns = document.getElementsByClassName('add-song')

for (var i=0; i <updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function () {
        var  songId = this.dataset.song
        var action = this.dataset.action
        console.log('songId:',songId,'action:',action)

        console.log('USER:', user)
        if (user === 'AnonymousUser'){
            console.log('Not logged in')
        }else {
            updateUserOrder(songId,action)
        }


    })

}

function updateUserOrder(songId,action){
    console.log('User is logged in , sending data...')

    var url = '/musicbeats/update_item/'

    fetch(url ,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,

        },
        body:JSON.stringify({'songId':songId, 'action':action})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data:',data)
        })
}