<template>
  <nav class="flex justify-between items-center px-20 py-0  border-b">
    
    <div class="flex items-center space-x-2 w-48"> 
      <img src="/chem.png" alt="ChemFind Logo" class="w-[100px]"> 
      <span class="font-bold text-xl">ChemFind</span>
    </div>

    <div class="flex items-center space-x-8">
      <router-link to="/" active-class="border-b-2 border-black pb-1 text-black" class="text-gray-700 hover:text-black-600">
        Home
      </router-link>
      <router-link to="/appPage" active-class="border-b-2 border-black pb-1 text-black" class="text-gray-700 hover:text-black-600">ChemFind</router-link>
      <router-link to="/history" active-class="border-b-2 border-black pb-1 text-black" class="text-gray-700 hover:text-black-600">History</router-link>
      <button 
      class="px-4 py-2 bg-gray-200 text-gray-700 font-semibold rounded-lg hover:bg-red-500 hover:text-white transition duration-200"
        @click="handleLogout"
      >
        Logout
      </button>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

  function handleLogout() {
  // Hapus semua indikator login
  localStorage.removeItem('user_id')
  localStorage.removeItem('token') // jika ada token
  router.push('/') // kembali ke home
}
</script>