'use client'

import { useState } from 'react'
import Link from 'next/link'
import { ChevronLeft, Heart, Bookmark } from 'lucide-react'
import { useParams } from 'next/navigation'

export default function ProductDetailPage() {
  const params = useParams()
  const id = params.id as string
  const [isFavorited, setIsFavorited] = useState(false)
  const [isBookmarked, setIsBookmarked] = useState(false)

  return (
    <div className="w-full max-w-screen-sm mx-auto">
      {/* Product Image */}
      <div className="relative aspect-square bg-surface">
        <img
          src={`/generic-product-display.png?height=400&width=400&query=product ${id}`}
          alt="Product"
          className="w-full h-full object-cover"
        />
        <Link
          href="/shop"
          className="absolute top-4 left-4 p-2 rounded-full bg-white/80 hover:bg-white"
        >
          <ChevronLeft className="w-6 h-6 text-foreground" />
        </Link>
      </div>

      {/* Product Info */}
      <div className="px-4 py-6 space-y-4">
        {/* Header with actions */}
        <div className="flex items-start justify-between">
          <div>
            <h1 className="text-2xl font-bold text-foreground">Judul</h1>
            <p className="text-sm text-muted mt-1">Suitable For warm tone</p>
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => setIsFavorited(!isFavorited)}
              className="p-2 rounded-full hover:bg-surface transition-colors"
            >
              <Heart
                className={`w-6 h-6 ${
                  isFavorited ? 'fill-heart text-heart' : 'text-heart'
                }`}
              />
            </button>
            <button
              onClick={() => setIsBookmarked(!isBookmarked)}
              className="p-2 rounded-full hover:bg-surface transition-colors"
            >
              <Bookmark
                className={`w-6 h-6 ${
                  isBookmarked
                    ? 'fill-bookmark text-bookmark'
                    : 'text-bookmark'
                }`}
              />
            </button>
          </div>
        </div>

        {/* Username and description */}
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded-full bg-surface" />
            <span className="text-sm font-medium text-foreground">Username</span>
          </div>
          <p className="text-sm text-muted">What's in here?</p>
        </div>

        {/* Tags */}
        <div className="flex flex-wrap gap-2">
          <span className="px-3 py-1 rounded-full bg-surface text-sm text-foreground border border-border">
            spill spill baju
          </span>
          <span className="px-3 py-1 rounded-full bg-surface text-sm text-foreground border border-border">
            spill spill celana
          </span>
        </div>

        {/* CTA Buttons */}
        <div className="flex gap-3 pt-4">
          <Link
            href={`/try-on?product=${id}`}
            className="flex-1 px-4 py-3 rounded-lg bg-primary text-white font-semibold hover:bg-primary-dark transition-colors text-center"
          >
            Virtual Try On
          </Link>
          <button className="flex-1 px-4 py-3 rounded-lg border border-primary text-primary font-semibold hover:bg-primary-light transition-colors">
            Add to Cart
          </button>
        </div>

        {/* Recommendation Section */}
        <div className="pt-4 border-t border-border">
          <h3 className="font-semibold text-foreground mb-3">Recommendation</h3>
          <div className="bg-surface rounded-lg aspect-square" />
        </div>
      </div>
    </div>
  )
}
