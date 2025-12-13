<template>
  <AppHeader />
  <div class="min-h-screen bg-white relative">
    <!-- MAIN CONTENT -->
    <div class="pt-14 pb-24 px-8 lg:px-16 flex flex-col items-center relative">

      <!-- Decorative molecule image -->
      <img
        src="/molekul_kiriR.png"
        class="hidden lg:block absolute left-0 top-16 w-[200px]"
        alt="Decoration"
      />

      <!-- PAGE TITLE -->
      <div class="text-center mb-14">
        <h1 class="text-4xl font-extrabold text-gray-900 tracking-tight">
          Chemical Compound Search
        </h1>
        <p class="text-gray-500 text-base mt-2">With Agentic AI</p>
      </div>

      <!-- RECOMMENDATIONS TITLE -->
      <h2 class="text-2xl font-bold text-center mb-10">Recommendations</h2>

      <!-- LOADING -->
      <div v-if="loading" class="text-center py-16">
        <p class="text-gray-600 text-lg">Loading recommendations...</p>
      </div>

      <!-- EMPTY -->
      <div v-else-if="recommendations.length === 0" class="text-center py-16">
        <p class="text-gray-600 text-lg">Tidak ada rekomendasi yang cocok.</p>
        <router-link
          to="/"
          class="text-blue-600 hover:underline mt-4 inline-block text-sm"
        >
          Kembali ke pencarian
        </router-link>
      </div>

      <!-- CARDS -->
      <div
        v-else
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 max-w-6xl mx-auto lg:ml-64 relative z-10"
      >
        <div
          v-for="(item, index) in recommendations"
          :key="index"
          class="bg-white border border-gray-200 rounded-xl p-6 flex flex-col items-center hover:shadow-xl transition-shadow duration-300"
        >
          <!-- IMAGE BOX -->
          <div
            class="w-full h-48 bg-gray-50 flex items-center justify-center rounded-lg mb-5 border border-gray-200"
          >
            <img
              v-if="item.image"
              :src="item.image"
              alt="Molecule Structure"
              class="object-contain h-full w-full p-4"
            />
            <div v-else class="text-gray-400 text-sm">No Image Available</div>
          </div>

          <!-- SMILES TEXT -->
          <div class="w-full text-center mb-5 px-2">
            <p class="text-sm text-gray-700 font-mono break-all leading-relaxed">
              {{ item.smiles }}
            </p>
          </div>

          <!-- BUTTON -->
          <button
            @click="goToDetail(item)"
            class="w-full bg-black text-white px-5 py-3 rounded-md text-sm font-semibold hover:bg-gray-800 active:bg-gray-900 transition"
          >
            View Detail
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import AppHeader from '../components/AppHeader.vue';
import { useRouter, useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";

const router = useRouter();
const route = useRoute();

const recommendations = ref([]);
const loading = ref(false);

// Ambil user_id dari localStorage, fallback ke 1 jika tidak ada
const userId = parseInt(localStorage.getItem("user_id")) || 1;

onMounted(async () => {
  let raw = route.params.results || route.query.results || null;
  if (!raw) return;

  try {
    const parsed = JSON.parse(raw);

    // Pastikan semua gambar base64 valid
    parsed.forEach((item) => {
      if (item.image && !item.image.startsWith("data:image")) {
        item.image = "data:image/png;base64," + item.image;
      }
    });

    recommendations.value = parsed;

    // --- Simpan ke history backend ---
    for (const item of recommendations.value) {
  try {
    await axios.post("http://127.0.0.1:8000/history/add", {
      user_id: userId,
      smiles: item.smiles ?? "",
      pIC50: item.pIC50 ?? item.pIc50 ?? null,  // frontend tetap pIC50
      atom_count: item.atom_count ?? null,
      logP: item.logP ?? null,
      justification: item.justification || "No justification available",
      image: item.image || null
    });
  } catch (err) {
    console.error("Failed to save history:", err.response?.data || err);
  }
}


  } catch (err) {
    console.error("Error parsing results:", err);
  }
});

function goToDetail(item) {
  sessionStorage.setItem("selectedCompound", JSON.stringify(item));
  router.push({
    path: "/detail",
    query: { smiles: item.smiles },
  });
}
</script>
