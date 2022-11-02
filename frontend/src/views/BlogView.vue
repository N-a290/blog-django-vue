<template>
  <div>
<<<<<<< HEAD
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
=======
    <h1>Here will be the blog page</h1>
  </div>
</template>
>>>>>>> 7134a108d00d79e9cdff2b8b397ca5054eec34eb
