new Vue({
  el: '#app-4',
  data: {
      todos: {"climbs": []}
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
