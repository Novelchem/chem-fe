<template>
  <nav class="flex justify-between items-center px-20 py-5 border-b bg-white fixed w-full top-0 z-50">
    
    <div class="flex items-center space-x-2 w-48"> 
      <img src="/chem.png" alt="ChemFind Logo" class="w-[100px]"> 
      <span class="font-bold text-xl">ChemFind</span>
    </div>

    <div class="flex items-center space-x-8">
      <a href="#overview" @click.prevent="scrollTo('overview')" 
         :class="{'border-b-2 border-black text-black': activeSection === 'overview'}"
         class="text-gray-700 hover:text-black cursor-pointer pb-1">
        Overview
      </a>
      <a href="#features" @click.prevent="scrollTo('features')" 
         :class="{'border-b-2 border-black text-black': activeSection === 'features'}"
         class="text-gray-700 hover:text-black cursor-pointer pb-1">
        Features
      </a>
      <a href="#how-to-use" @click.prevent="scrollTo('how-to-use')" 
         :class="{'border-b-2 border-black text-black': activeSection === 'how-to-use'}"
         class="text-gray-700 hover:text-black cursor-pointer pb-1">
        How to use
      </a>
      <a href="#contact" @click.prevent="scrollTo('contact')" 
         :class="{'border-b-2 border-black text-black': activeSection === 'contact'}"
         class="text-gray-700 hover:text-black cursor-pointer pb-1">
        Contact
      </a>
    </div>

    <router-link to="/auth" class="bg-black text-white px-5 py-2 rounded-md hover:bg-gray-800">
      Login/Register
    </router-link>

  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('overview')

const scrollTo = (id) => {
  const element = document.getElementById(id)
  if (element) {
    const offsetTop = element.offsetTop - 80 // 80px untuk navbar
    window.scrollTo({
      top: offsetTop,
      behavior: 'smooth'
    })
  }
}

// Deteksi section mana yang sedang aktif saat scroll
const handleScroll = () => {
  const sections = ['overview', 'features', 'how-to-use', 'contact']
  
  for (const section of sections) {
    const element = document.getElementById(section)
    if (element) {
      const rect = element.getBoundingClientRect()
      if (rect.top <= 100 && rect.bottom >= 100) {
        activeSection.value = section
        break
      }
    }
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>