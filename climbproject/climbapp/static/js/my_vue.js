new Vue({
  el: '#app-4',
  data: {
  //  return {
      todos: {"climbs": []}
    //}
    // climbs: []
  },
  mounted() {
    axios
      .get('/climbs/')
      .then(response => (this.todos = response.data))
    setInterval(function (){
      axios
      .get('/climbs/')
      .then(response => (this.todos = response.data))
      console.log(this.todos);
    }.bind(this), 10000);
  }
})

  // //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  // created: function() {
  //       this.fetchclimbList();
  //       this.timer = setInterval(this.fetchClimbList, 3000);
  // },
  // methods: {
  //   fetchClimbList: function() {
  //       axios
  //         .get('/climbs/')
  //         .then(response => (this.climbs = response.data.climbs))
  //   },
  //   cancelAutoUpdate: function() { clearInterval(this.timer) }
  // },
  // beforeDestroy() {
  //   clearInterval(this.timer)
  // }

// })
