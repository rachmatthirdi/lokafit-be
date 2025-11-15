'use client'

import Link from 'next/link'
import { LogOut, Settings } from 'lucide-react'

export default function ProfilePage() {
  return (
    <div className="w-full max-w-screen-sm mx-auto px-4 py-6 space-y-6">
      {/* Header */}
      <h1 className="text-2xl font-bold text-foreground">Profile</h1>

      {/* Profile Card */}
      <div className="bg-surface rounded-lg p-6 space-y-4 border border-border">
        <div className="flex items-center gap-4">
          <div className="w-16 h-16 rounded-full bg-primary text-white flex items-center justify-center text-2xl font-bold">
            W
          </div>
          <div>
            <p className="text-lg font-semibold text-foreground">Wyena</p>
            <p className="text-sm text-muted">@wyena_username</p>
          </div>
        </div>
        <p className="text-sm text-foreground">Warm Skin Tone</p>
      </div>

      {/* Menu Items */}
      <div className="space-y-2">
        <Link
          href="/profile/edit"
          className="flex items-center gap-3 p-4 bg-surface rounded-lg border border-border hover:border-primary transition-colors"
        >
          <Settings className="w-5 h-5 text-primary" />
          <span className="text-foreground font-medium">Edit Profile</span>
        </Link>
      </div>

      {/* Logout Button */}
      <button className="w-full flex items-center justify-center gap-2 px-4 py-3 rounded-lg bg-error text-white font-semibold hover:opacity-90 transition-opacity">
        <LogOut className="w-5 h-5" />
        Logout
      </button>
    </div>
  )
}
