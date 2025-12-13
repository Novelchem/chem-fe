<template>
  <div>
    <!-- Overview Section -->
    <section id="overview" class="min-h-screen flex items-center justify-center bg-white">
      <div class="flex items-center justify-between px-20 w-full">
        <div class="max-w-lg space-y-5">
          <h1 class="text-5xl font-bold leading-tight">
            Explore Chemical<br />Discoverment
          </h1>
          <p class="text-gray-600">
            Explore the world of chemistry with intelligent assistance.
            Powered by agentic AI, our system recommends chemical insights that match your curiosity and learning goals.
            Discover more, learn faster, and see chemistry from a new perspective.
          </p>

          <button
            @click="goToApp"
            class="inline-block bg-[#4A70A9] text-white px-6 py-3 rounded-md mt-8 hover:bg-[#3A5D8A] transition duration-150 ease-in-out"
          >
            Try it Now!
          </button>
        </div>

        <img src="/molekul.png" class="w-[360px]" alt="Molecule" />
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="min-h-screen relative overflow-hidden flex items-center justify-center">
      <img src="/molekul_kiriF.png" alt="ChemFind Logo" class="absolute top-0 left-0 w-[240px] h-[200px] z-0">

      <div class="absolute inset-0 h-full w-full bg-gradient-to-b from-white to-[#4A70A9] opacity-70 z-0"></div>

      <div class="relative z-10 w-full">
        <div class="px-4 md:px-8 text-center">
          <h2 class="text-4xl md:text-5xl font-extrabold mb-16 text-gray-900">
            Features
          </h2>

          <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 mb-10">
            <div class="bg-[#4A70A9] text-white p-6 rounded-xl shadow-2xl shadow-gray-700/80 h-80 flex flex-col justify-center items-center">
              <img src="/agentic_ai.png" alt="Icon 1" class="w-20 h-20 mb-4">
              <h3 class="text-2xl font-bold mb-2">Agentic AI System</h3>
              <p class="text-white text-sm max-w-xs leading-relaxed">
                AI-powered assistant that autonomously processes chemical data.
              </p>
            </div>

            <div class="bg-[#4A70A9] text-white p-6 rounded-xl shadow-2xl shadow-gray-700/80 h-80 flex flex-col justify-center items-center">
              <img src="/pointer.png" alt="Icon 2" class="w-20 h-20 mb-4">
              <h3 class="text-2xl font-bold mb-2">Easy To Use</h3>
              <p class="text-white text-sm max-w-xs leading-relaxed">
                Easy to Use, makes chemical exploration accessible for everyone.
              </p>
            </div>

            <div class="bg-[#4A70A9] text-white p-6 rounded-xl shadow-2xl shadow-gray-700/80 h-80 flex flex-col justify-center items-center">
              <img src="/search.png" alt="Icon 3" class="w-20 h-20 mb-4">
              <h3 class="text-2xl font-bold mb-2">Molecular Similarity Search</h3>
              <p class="text-white text-sm max-w-xs leading-relaxed">
                Find and compare similar chemical structures from extensive molecular instantly.
              </p>
            </div>
          </div>
          
        </div>
      </div>
      
      <img src="/molekul_kananF.png" alt="ChemFind Logo" class="absolute bottom-0 right-0 w-[200px] h-[200px] z-0">
    </section>

    <!-- How To Use Section -->
    <section id="how-to-use" class="min-h-screen relative overflow-hidden bg-white flex items-center justify-center">
      <img src="/molekul_kiri_atasH.png" alt="ChemFind Logo" class="absolute top-0 left-0 w-[200px] h-[160px] z-0">
      
      <div class="absolute inset-0 opacity-20 bg-no-repeat bg-cover z-0" style="background-color: #f7f9fc;"></div>
      
      <div class="relative z-10 w-full px-4 md:px-8 text-center">
        <h2 class="text-4xl md:text-5xl font-extrabold mb-16 text-gray-900">
          How To Use
        </h2>

        <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 mb-10">
          <div class="bg-black text-white p-6 rounded-xl shadow-2xl shadow-gray-700/80 h-80 flex flex-col justify-center items-center">
            <p class="text-7xl font-extrabold mb-4">1</p>
            <h3 class="text-2xl font-bold mb-2">Enter Input</h3>
            <p class="text-white text-sm max-w-xs leading-relaxed">
              Enter text or data related to the desired chemical topic. xxxxx
            </p>
          </div>

          <div class="bg-black text-white p-6 rounded-xl shadow-2xl shadow-gray-700/80 h-80 flex flex-col justify-center items-center">
            <p class="text-7xl font-extrabold mb-4">2</p>
            <h3 class="text-2xl font-bold mb-2">AI Processing</h3>
            <p class="text-white text-sm max-w-xs leading-relaxed">
              The system will analyzes the input and generates recommendations
            </p>
          </div>

          <div class="bg-black text-white p-6 rounded-xl shadow-2xl shadow-gray-700/80 h-80 flex flex-col justify-center items-center">
            <p class="text-7xl font-extrabold mb-4">3</p>
            <h3 class="text-2xl font-bold mb-2">View Output</h3>
            <p class="text-white text-sm max-w-xs leading-relaxed">
              Relevant results and insights are displayed for further exploration.
            </p>
          </div>
        </div>
      </div>
      
      <img src="/molekul_bawah.png" alt="ChemFind Logo" class="absolute bottom-0 left-0 w-[370px] h-[320px] z-0">
    </section>

    <!-- Contact Section -->
    <section id="contact" class="min-h-screen flex flex-col justify-between bg-white">
      <div class="flex-1 flex items-center justify-center">
        <div class="text-center py-20">
          <h2 class="text-4xl md:text-5xl font-extrabold mb-6 text-gray-900">
            Get In Touch
          </h2>
          <p class="text-gray-600 text-lg mb-8 max-w-2xl mx-auto">
            Have questions about ChemFind? Want to collaborate or learn more about our platform? We'd love to hear from you.
          </p>
          <a href="https://github.com/Novelchem" 
            target="_blank" 
            rel="noopener noreferrer"
            class="inline-block bg-[#4A70A9] text-white px-8 py-3 rounded-lg text-lg font-medium hover:bg-[#3A5D8A] transition shadow-lg">
            Contact Us
          </a>
        </div>
      </div>
      <Footer />
    </section>

  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import Footer from '../components/Footer.vue'

const router = useRouter()

function goToApp() {
  const userId = localStorage.getItem("user_id")

  if (!userId || userId === "null" || userId === undefined) {
    router.push({ path: '/auth' })
  } else {
    router.push({ path: '/AppPage' })
  }
}
</script>