<template>
  <div>
    <h1>BLOG</h1>
  </div>
  <div>
    <div v-for="post in APIData" :key="post.id">
      <div>
        <h1>{{ post.title }}</h1>
        <p>{{ post.excerpt }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Blog',
  data () {
    return {
      APIData: []
    }
  },
  mounted() {
    this.getAPIData()
  },
  methods: {
    getAPIData() {
      axios
        .get('/blog/posts/')
        .then(response => {
          this.APIData = response.data
        })
        .catch(error => {
          console.log(error.data)
        })
    }
  }
}

</script>