<template>
  <el-row>
    <el-col :span="8" :offset="8">
      <el-form :model="form" label-width="80px">
        <h2>Login 1</h2>
        <el-form-item label="Username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="form.password" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">Submit</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>

<script>
  import store from '../store'

  let Base64 = require('js-base64').Base64

  export default {
    name: "Login1",
    data() {
      return {
        form: {
          username: null,
          password: null,
        }
      }
    },
    methods: {
      onSubmit() {
        let token = Base64.encode(JSON.stringify(this.form))
        this.$http.post(store.state.url.root, {
          token: token
        }).then((data) => {
          console.log('data', data)
        })
      }
    }
  }
</script>

<style scoped>
  form {
    margin-top: 100px;
  }

  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
</style>