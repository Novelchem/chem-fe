<template>
<div class="h-screen relative overflow-hidden flex items-center justify-center">
    <img src="/molekul_kiriF.png" alt="ChemFind Logo" class="absolute top-0 left-0 w-[240px] h-[200px] z-0">

    <div class="absolute inset-0 h-full w-full bg-gradient-to-b from-white to-[#4A70A9] opacity-70 z-0">
    </div>

    <div class="relative z-10 w-full">
        <section class="px-4 md:px-8 text-center">
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
        </section>
    </div>
    
    <img src="/molekul_kananF.png" alt="ChemFind Logo" class="absolute bottom-0 right-0 w-[200px] h-[200px] z-0">
</div>
</template>