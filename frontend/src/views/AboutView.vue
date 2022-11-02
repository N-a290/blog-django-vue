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
import { getAPI } from '@/axios-api';

export default {
  name: 'Blog',
  data () {
    return {
      APIData: []
    }
  },
  created () {
        getAPI.get('/blog/posts/',)
          .then(response => {
            console.log('Post API has received data')
            this.APIData = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
}

</script>