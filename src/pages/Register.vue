<template>
  <div class="min-h-screen flex items-center justify-center">
    <button 
      class="absolute top-5 left-5  px-3 py-1 rounded hover:bg-[#8FABD4] text-5xl"
      @click="$router.push('/')"
    >
      🡐
    </button>
    <div class="max-w-6xl w-full flex bg-white shadow-xl rounded-xl overflow-hidden min-h-[600px]">
      <div class="w-full lg:w-1/2 p-10 flex flex-col justify-center relative h-full">
        <div class="absolute top-6 left-10 flex items-center">
          <img src="/chem.png" alt="ChemFind Logo" class="w-[100px]"> 
          <span class="ml-2 font-bold text-lg text-gray-800">ChemFind</span>
        </div>

        <h2 class="text-4xl font-bold text-gray-800 mb-8 mt-24 text-center">Sign Up</h2>

        <form @submit.prevent="handleRegister" class="space-y-6 pb-36">
          <div>
            <input
              type="email"
              placeholder="Email"
              v-model="email"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>
          <div>
            <input
              type="password"
              placeholder="Password"
              v-model="password"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <div>
            <input
              type="password"
              placeholder="Confirm Password"
              v-model="confirmPassword"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg bg-gray-200 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              required
            />
          </div>

          <button
            type="submit"
            class="w-full py-3 bg-[#4A70A9] text-white font-semibold rounded-lg shadow-md"
            :disabled="loading"
          >
            {{ loading ? "Signing Up..." : "Sign Up" }}
          </button>

          <p v-if="error" class="text-red-600 text-center font-semibold mt-2">{{ error }}</p>
          <p v-if="success" class="text-green-600 text-center font-semibold mt-2">{{ success }}</p>

        </form>
        <img src="/molekul_bawah.png" alt="ChemFind Logo" class="absolute bottom-0 left-0 w-[280px] h-[220px]">
      </div>

      <div class="hidden lg:block lg:w-1/2 p-12 bg--700 text-white relative">
        <div class="absolute inset-0 bg-[#4A70A9] rounded-l-[350px]"></div>

        <div class="relative z-10 h-full flex flex-col items-center justify-center text-center space-y-6">
          <h2 class="text-4xl font-light">Hello, Friend!</h2>
          <p class="text-sm max-w-xs">
            Login your account to use all of site features
          </p>
          <router-link
            to="/auth"
            class="mt-4 px-10 py-3 border-2 border-white text-white font-semibold rounded-lg hover:bg-white hover:text-[#4A70A9] transition duration-300"
          >
            Sign In
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: "Register",
  setup() {
    const router = useRouter()
    const email = ref("")
    const password = ref("")
    const confirmPassword = ref("")
    const error = ref("")
    const success = ref("")
    const loading = ref(false)

    const handleRegister = async () => {
      if (!email.value || !password.value || !confirmPassword.value) {
        error.value = "All fields must be filled"
        return
      }

      if (password.value !== confirmPassword.value) {
        error.value = "Passwords do not match"
        return
      }

      loading.value = true
      error.value = ""
      success.value = ""

      try {
        const res = await fetch("http://127.0.0.1:8000/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: email.value,
            email: email.value,
            password: password.value
          })
        })

        const data = await res.json()

        if (res.ok) {
          success.value = "Registration successful! Please log in."
          setTimeout(() => {
            router.push("/auth")
          }, 1000)
        } else {
          error.value = data.detail || "Registration failed"
        }
      } catch (err) {
        error.value = "Failed to contact the server"
      } finally {
        loading.value = false
      }
    }

    return {
      email,
      password,
      confirmPassword,
      error,
      success,
      loading,
      handleRegister
    }
  }
}
</script>

<style scoped>
</style>
