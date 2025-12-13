<template>
  <AppHeader />
  <div class="min-h-screen bg-white">
    <div class="pt-12 pb-20 px-8 lg:px-12 flex flex-col lg:flex-row items-start space-y-10 lg:space-y-0 lg:space-x-16 max-w-7xl mx-auto">
      
      <!-- Left Side - Molecule Image -->
      <div class="flex-shrink-0 w-full max-w-sm lg:w-96">
        <div class="bg-gray-50 rounded-lg p-6 border border-gray-200">
          <img v-if="moleculeImage"
               :src="moleculeImage"
               class="w-full h-auto object-contain"
               alt="Molecule Structure" />
          <img v-else
               src="/molekul.png"
               class="w-full h-auto object-contain opacity-50"
               alt="Default Molecule" />
        </div>
      </div>

      <!-- Right Side - Chemical Details -->
      <div class="flex-1 max-w-2xl">
        <h1 class="text-3xl font-bold text-gray-900 mb-8">Chemical Details</h1>

        <!-- SMILES -->
        <div class="mb-6 pb-6 border-b border-gray-300">
          <h2 class="text-base font-bold text-gray-800 mb-3">SMILES</h2>
          <p class="text-sm text-gray-700 font-mono break-all leading-relaxed bg-gray-50 p-3 rounded">
            {{ smiles || 'N/A' }}
          </p>
        </div>

        <!-- Properties -->
        <div class="mb-6 pb-6 border-b border-gray-300">
          <h2 class="text-base font-bold text-gray-800 mb-4">Properties</h2>
          <div class="space-y-3 text-sm">
            <div class="flex justify-between items-center py-2 px-3 bg-gray-50 rounded">
              <span class="text-gray-700 font-medium">pIC50:</span>
              <span class="font-bold text-gray-900">{{ properties.pic50 }}</span>
            </div>
            <div class="flex justify-between items-center py-2 px-3 bg-gray-50 rounded">
              <span class="text-gray-700 font-medium">Atom Count:</span>
              <span class="font-bold text-gray-900">{{ properties.atom_count || 'N/A' }}</span>
            </div>
            <div class="flex justify-between items-center py-2 px-3 bg-gray-50 rounded">
              <span class="text-gray-700 font-medium">LogP:</span>
              <span class="font-bold text-gray-900">{{ properties.logP || 'N/A' }}</span>
            </div>
          </div>
        </div>

        <!-- Justification -->
        <div class="mb-8">
          <h2 class="text-base font-bold text-gray-800 mb-4">Justifications</h2>
          <div class="bg-gray-50 border border-gray-200 p-5 rounded-lg text-sm text-gray-800 leading-relaxed">
            {{ justification || 'No justification available for this compound.' }}
          </div>
        </div>

        <!-- Back Button -->
        <div class="mt-10">
          <button
            @click="goBack"
            class="bg-black text-white px-6 py-3 rounded-md text-sm font-semibold hover:bg-gray-800 active:bg-gray-900 transition-colors duration-200 flex items-center space-x-2">
            <span>←</span>
            <span>Back to Results</span>
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import AppHeader from '../components/AppHeader.vue'
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const smiles = ref('')
const moleculeImage = ref('')
const properties = ref({
  pic50: 'N/A',
  atom_count: 'N/A',
  logP: 'N/A'
})
const justification = ref('')

// Ambil data dari sessionStorage (predict) atau fallback route query (history)
onMounted(() => {
  const storedData = sessionStorage.getItem('selectedCompound')
  if (storedData) {
    const data = JSON.parse(storedData)
    smiles.value = data.smiles || ''
    moleculeImage.value = data.image || null
    properties.value = {
      pic50: data.pIC50 ?? data.properties?.pic50 ?? 'N/A',
      atom_count: data.atom_count ?? data.properties?.atom_count ?? 'N/A',
      logP: data.logP ?? data.properties?.logP ?? 'N/A'
    }
    justification.value = data.justification || ''
    sessionStorage.removeItem('selectedCompound')
  } else if (route.query.data) {
    const data = JSON.parse(route.query.data)
    smiles.value = data.smiles || route.query.smiles || ''
    moleculeImage.value = null // history tidak punya image
    properties.value = {
      pic50: data.pIC50 ?? data.properties?.pic50 ?? 'N/A',
      atom_count: data.atom_count ?? data.properties?.atom_count ?? 'N/A',
      logP: data.logP ?? data.properties?.logP ?? 'N/A'
    }
    justification.value = data.justification || ''
  } else if (route.query.smiles) {
    smiles.value = route.query.smiles
    moleculeImage.value = null
  }
})

function goBack() {
  router.back()
}
</script>
