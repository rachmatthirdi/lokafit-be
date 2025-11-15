'use client'

import Link from 'next/link'
import { Plus } from 'lucide-react'

export default function WardrobePage() {
  const wardrobeItems = [
    { id: 1, name: 'T-Shirt', count: 12, image: '/plain-white-tshirt.png' },
    { id: 2, name: 'Blouse', count: 8, image: '/elegant-silk-blouse.png' },
    { id: 3, name: 'Outer', count: 5, image: '/outer-jacket.jpg' },
    { id: 4, name: 'Jacket', count: 6, image: '/stylish-woman-leather-jacket.png' },
  ]

  return (
    <div className="w-full max-w-screen-sm mx-auto px-4 py-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-foreground">Wyena's Digital Wardrobe</h1>
        <Link
          href="/wardrobe/scan"
          className="p-2 rounded-full bg-primary text-white hover:bg-primary-dark transition-colors"
        >
          <Plus className="w-6 h-6" />
        </Link>
      </div>

      {/* Wardrobe Items */}
      <div className="space-y-3">
        {wardrobeItems.map((item) => (
          <Link
            key={item.id}
            href={`/wardrobe/${item.id}`}
            className="flex items-center gap-4 p-4 bg-surface rounded-lg border border-border hover:border-primary transition-colors"
          >
            <div className="w-16 h-16 rounded-lg bg-gray-300 overflow-hidden flex-shrink-0">
              <img
                src={item.image || "/placeholder.svg"}
                alt={item.name}
                className="w-full h-full object-cover"
              />
            </div>
            <div className="flex-1">
              <p className="font-semibold text-foreground">{item.name}</p>
              <p className="text-sm text-muted">{item.count} items</p>
            </div>
            <p className="text-lg font-semibold text-primary">{item.count}</p>
          </Link>
        ))}
      </div>

      {/* Atasan Section */}
      <div className="pt-4 space-y-3">
        <h2 className="font-semibold text-foreground">Atasan</h2>
        <div className="grid grid-cols-2 gap-3">
          {[1, 2, 3, 4].map((i) => (
            <div
              key={i}
              className="bg-surface rounded-lg aspect-square overflow-hidden border border-border"
            >
              <img
                src={`/generic-clothing-item.png?height=160&width=160&query=clothing item ${i}`}
                alt={`Item ${i}`}
                className="w-full h-full object-cover"
              />
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
