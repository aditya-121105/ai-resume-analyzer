import { FileText } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 w-full border-b bg-white/80 backdrop-blur">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">

        {/* Logo */}
        <div className="flex items-center gap-2">
          <FileText className="h-6 w-6 text-blue-600" />
          <span className="text-xl font-bold tracking-tight">
            ResumeGuide
          </span>
        </div>

        {/* Navigation */}
        <nav className="hidden md:flex items-center gap-8">
          <a
            href="#features"
            className="text-sm font-medium text-slate-600 transition hover:text-slate-900"
          >
            Features
          </a>

          <a
            href="#how-it-works"
            className="text-sm font-medium text-slate-600 transition hover:text-slate-900"
          >
            How It Works
          </a>
        </nav>

        {/* Actions */}
        <div className="flex items-center gap-3">
          <Button variant="ghost">
            Login
          </Button>

          <Button>
            Start Free Analysis
          </Button>
        </div>

      </div>
    </header>
  );
}