'use client'

import { useState } from 'react'
import Link from 'next/link'
import { Heart, Search } from 'lucide-react'

export default function HomePage() {
  const [selectedDay, setSelectedDay] = useState('Monday')

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
  const outfitRecommendations = [
    {
      id: 1,
      name: 'Recommendation Outfit',
      image: '/casual-outfit-top.jpg',
    },
    {
      id: 2,
      name: 'Alternative Outfit',
      image: '/casual-outfit-bottom.jpg',
    },
  ]

  return (
    <div className="w-full max-w-screen-sm mx-auto px-4 py-6 space-y-6">
      {/* Header */}
      <div className="space-y-4">
        <h1 className="text-2xl font-bold text-foreground">home</h1>
      </div>

      {/* Search Bar */}
      <div className="relative">
        <Search className="absolute left-3 top-3 w-5 h-5 text-muted" />
        <input
          type="text"
          placeholder="Search"
          className="w-full pl-10 pr-4 py-2 rounded-lg border border-border bg-surface text-foreground placeholder-muted focus:outline-none focus:ring-2 focus:ring-primary"
        />
      </div>

      {/* Daily Outfit Recommendation */}
      <div className="space-y-3">
        <h2 className="font-semibold text-foreground">Daily Outfit Recommendation</h2>
        <div className="flex gap-2 overflow-x-auto pb-2">
          {days.map((day) => (
            <button
              key={day}
              onClick={() => setSelectedDay(day)}
              className={`px-4 py-2 rounded-full whitespace-nowrap transition-colors ${
                selectedDay === day
                  ? 'bg-primary text-white'
                  : 'bg-surface text-foreground border border-border'
              }`}
            >
              {day}
            </button>
          ))}
        </div>
      </div>

      {/* Recommendation Grid */}
      <div className="grid grid-cols-2 gap-4">
        {outfitRecommendations.map((outfit) => (
          <Link
            key={outfit.id}
            href={`/product/${outfit.id}`}
            className="space-y-2 group"
          >
            <div className="bg-surface rounded-lg overflow-hidden aspect-square relative">
              <img
                src={outfit.image || "/placeholder.svg"}
                alt={outfit.name}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform"
              />
              <button className="absolute top-2 right-2 p-2 rounded-full bg-white/80 hover:bg-white transition-colors">
                <Heart className="w-5 h-5 text-heart" />
              </button>
            </div>
            <p className="text-sm font-medium text-foreground">{outfit.name}</p>
          </Link>
        ))}
      </div>

      {/* Recommendation Section */}
      <div className="space-y-3">
        <h2 className="font-semibold text-foreground">Recommendation</h2>
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-surface rounded-lg aspect-square flex items-center justify-center">
            <img
              src="/fashion-item-1.jpg"
              alt="Recommended item 1"
              className="w-full h-full object-cover rounded-lg"
            />
          </div>
          <div className="bg-surface rounded-lg aspect-square flex items-center justify-center">
            <img
              src="/fashion-item-2.jpg"
              alt="Recommended item 2"
              className="w-full h-full object-cover rounded-lg"
            />
          </div>
        </div>
      </div>
    </div>
  )
}
