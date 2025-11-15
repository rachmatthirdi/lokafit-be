'use client'

import { useState } from 'react'
import Link from 'next/link'
import { Search, Heart } from 'lucide-react'

export default function ShopPage() {
  const [favorites, setFavorites] = useState<number[]>([])

  const products = [
    { id: 1, name: 'Blue Dress', price: 'Rp 299.000', image: '/blue-dress.png' },
    { id: 2, name: 'White Blouse', price: 'Rp 199.000', image: '/white-blouse.png' },
    { id: 3, name: 'Black Jacket', price: 'Rp 399.000', image: '/black-jacket.png' },
    { id: 4, name: 'Beige Pants', price: 'Rp 249.000', image: '/beige-pants.jpg' },
    { id: 5, name: 'Red Skirt', price: 'Rp 279.000', image: '/flowing-red-skirt.png' },
    { id: 6, name: 'Green Sweater', price: 'Rp 229.000', image: '/green-sweater.png' },
  ]

  const toggleFavorite = (id: number) => {
    setFavorites((prev) =>
      prev.includes(id) ? prev.filter((fav) => fav !== id) : [...prev, id]
    )
  }

  return (
    <div className="w-full max-w-screen-sm mx-auto px-4 py-6 space-y-6">
      {/* Header */}
      <h1 className="text-2xl font-bold text-foreground">Shop</h1>

      {/* Search Bar */}
      <div className="relative">
        <Search className="absolute left-3 top-3 w-5 h-5 text-muted" />
        <input
          type="text"
          placeholder="Search products"
          className="w-full pl-10 pr-4 py-2 rounded-lg border border-border bg-surface text-foreground placeholder-muted focus:outline-none focus:ring-2 focus:ring-primary"
        />
      </div>

      {/* Product Grid */}
      <div className="grid grid-cols-2 gap-4">
        {products.map((product) => (
          <div key={product.id} className="space-y-2">
            <Link
              href={`/product/${product.id}`}
              className="block bg-surface rounded-lg overflow-hidden aspect-[3/4] relative group"
            >
              <img
                src={product.image || "/placeholder.svg"}
                alt={product.name}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform"
              />
              <button
                onClick={(e) => {
                  e.preventDefault()
                  toggleFavorite(product.id)
                }}
                className="absolute top-2 right-2 p-2 rounded-full bg-white/80 hover:bg-white transition-colors"
              >
                <Heart
                  className={`w-5 h-5 ${
                    favorites.includes(product.id)
                      ? 'fill-heart text-heart'
                      : 'text-heart'
                  }`}
                />
              </button>
            </Link>
            <div>
              <Link href={`/product/${product.id}`} className="hover:underline">
                <p className="text-sm font-medium text-foreground line-clamp-1">
                  {product.name}
                </p>
              </Link>
              <p className="text-sm text-muted-light font-semibold">
                {product.price}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
