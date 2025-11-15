'use client'

import { useState } from 'react'
import Link from 'next/link'
import { ChevronLeft, ChevronRight } from 'lucide-react'

export default function VirtualTryOnPage() {
  const [currentOutfit, setCurrentOutfit] = useState(0)
  const [selectedCategory, setSelectedCategory] = useState('shirt')

  const outfits = [
    { id: 1, category: 'shirt', image: '/white-shirt.png' },
    { id: 2, category: 'pants', image: '/blue-pants.jpg' },
  ]

  const categories = ['T-Shirt', 'Blouse', 'Outer', 'Jacket']

  return (
    <div className="w-full max-w-screen-sm mx-auto flex flex-col h-screen">
      {/* Header */}
      <div className="px-4 py-4 border-b border-border">
        <h1 className="text-xl font-bold text-foreground text-center">
          Virtual Try On
        </h1>
      </div>

      {/* Manekin Area */}
      <div className="flex-1 flex items-center justify-center bg-surface px-4 py-8">
        <div className="relative w-full max-w-xs">
          {/* Manekin placeholder */}
          <div className="bg-gray-300 rounded-lg aspect-[9/16] flex items-center justify-center mb-4">
            <img
              src="/fashion-manekin-model.jpg"
              alt="Manekin"
              className="w-full h-full object-cover rounded-lg"
            />
          </div>

          {/* Navigation buttons */}
          <div className="absolute inset-0 flex items-center justify-between pointer-events-none">
            <button className="pointer-events-auto p-2 rounded-full bg-white/70 hover:bg-white text-foreground">
              <ChevronLeft className="w-6 h-6" />
            </button>
            <button className="pointer-events-auto p-2 rounded-full bg-white/70 hover:bg-white text-foreground">
              <ChevronRight className="w-6 h-6" />
            </button>
          </div>
        </div>
      </div>

      {/* Category Selection */}
      <div className="px-4 py-4 bg-background border-t border-border space-y-3">
        <h2 className="font-semibold text-foreground text-center">Atasan</h2>
        <div className="flex flex-col gap-2">
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => setSelectedCategory(category.toLowerCase())}
              className={`px-4 py-3 rounded-lg border transition-colors ${
                selectedCategory === category.toLowerCase()
                  ? 'bg-primary text-white border-primary'
                  : 'bg-surface text-foreground border-border'
              }`}
            >
              {category}
            </button>
          ))}
        </div>

        {/* Fit Perfectly Button */}
        <button className="w-full px-4 py-3 mt-4 rounded-lg bg-gray-300 text-foreground font-semibold hover:bg-gray-400 transition-colors">
          Fit Perfectly
        </button>
      </div>
    </div>
  )
}
