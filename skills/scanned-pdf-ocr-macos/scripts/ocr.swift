import Foundation
import PDFKit
import Vision
import CoreGraphics

let args = CommandLine.arguments
guard args.count >= 2 else {
    FileHandle.standardError.write("usage: ocr <pdf> [startPage] [endPage]\n".data(using: .utf8)!)
    exit(2)
}
let pdfPath = args[1]
let startPage = args.count > 2 ? (Int(args[2]) ?? 1) : 1
let endPage   = args.count > 3 ? (Int(args[3]) ?? Int.max) : Int.max

guard let doc = PDFDocument(url: URL(fileURLWithPath: pdfPath)) else {
    FileHandle.standardError.write("cannot open pdf\n".data(using: .utf8)!); exit(1)
}
let total = doc.pageCount
let last = min(endPage, total)

for i in (startPage - 1)..<last {
    guard let page = doc.page(at: i) else { continue }
    let bounds = page.bounds(for: .mediaBox)
    let scale = max(1.0, 2000.0 / bounds.width)
    let w = Int(bounds.width * scale), h = Int(bounds.height * scale)

    let cs = CGColorSpaceCreateDeviceRGB()
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8,
                              bytesPerRow: 0, space: cs,
                              bitmapInfo: CGImageAlphaInfo.premultipliedFirst.rawValue) else { continue }
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx)
    guard let cg = ctx.makeImage() else { continue }

    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["zh-Hans", "en-US"]
    req.usesLanguageCorrection = true
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    do { try handler.perform([req]) } catch { continue }

    print("===== PAGE \(i + 1) =====")
    for obs in req.results ?? [] {
        if let c = obs.topCandidates(1).first { print(c.string) }
    }
    FileHandle.standardError.write("done \(i + 1)/\(last)\r".data(using: .utf8)!)
}
FileHandle.standardError.write("\n".data(using: .utf8)!)
