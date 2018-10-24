var app4 = new Vue({
  el: '#app-4',
  data: {
    climbs: []
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchclimbList();
        this.timer = setInterval(this.fetchClimbList, 3000);
  },
  methods: {
    fetchClimbList: function() {
        // $.get('/suggestions/', function(suggest_list) {
        //     this.suggestions = suggest_list.suggestions;
        //     console.log(suggest_list);
        // }.bind(this));
        axios
          .get('/climbs/')
          .then(response => (this.climbs = response.data.climbs))
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }
})
