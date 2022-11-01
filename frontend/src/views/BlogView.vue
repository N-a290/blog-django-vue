<template>
  <div>
    <h1>BLOG</h1>
  </div>
  <div>
    <div v-for="post in APIdata" :key="post.id">
      <div>
        <p>{{ post.title }}</p>
        <p>{{ post.excerpt }}</p>
      </div>
    </div>
  </div>
</template>
