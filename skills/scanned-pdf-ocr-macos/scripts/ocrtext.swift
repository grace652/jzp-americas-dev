import Foundation
import PDFKit
import Vision
import CoreGraphics
import CoreText
import AppKit

let a = CommandLine.arguments
guard a.count >= 3 else { FileHandle.standardError.write("usage: ocrpdf <in.pdf> <out.pdf> [start] [end]\n".data(using: .utf8)!); exit(2) }
let inPath = a[1], outPath = a[2]
let startP = a.count > 3 ? (Int(a[3]) ?? 1) : 1
let endP   = a.count > 4 ? (Int(a[4]) ?? Int.max) : Int.max

guard let doc = PDFDocument(url: URL(fileURLWithPath: inPath)) else { exit(1) }
let total = doc.pageCount
let last = min(endP, total)

guard let ctx = CGContext(URL(fileURLWithPath: outPath) as CFURL, mediaBox: nil, nil) else { exit(1) }
let fontName = "PingFangSC-Regular" as CFString

for i in (startP - 1)..<last {
    guard let page = doc.page(at: i) else { continue }
    let box = page.bounds(for: .mediaBox)
    let w = box.width, h = box.height
    let scale = max(1.0, 2000.0 / w)

    let cs = CGColorSpaceCreateDeviceRGB()
    guard let ictx = CGContext(data: nil, width: Int(w*scale), height: Int(h*scale),
                               bitsPerComponent: 8, bytesPerRow: 0, space: cs,
                               bitmapInfo: CGImageAlphaInfo.premultipliedFirst.rawValue) else { continue }
    ictx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ictx.fill(CGRect(x: 0, y: 0, width: w*scale, height: h*scale))
    ictx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ictx)
    guard let cg = ictx.makeImage() else { continue }

    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["zh-Hans", "en-US"]
    req.usesLanguageCorrection = true
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])

    ctx.beginPDFPage([kCGPDFContextMediaBox as String: NSValue(rect: box)] as CFDictionary)

    ctx.saveGState()
    ctx.setTextDrawingMode(.invisible)
    for obs in req.results ?? [] {
        guard let c = obs.topCandidates(1).first else { continue }
        let bb = obs.boundingBox
        let rh = bb.height * h
        let x = bb.minX * w, y = bb.minY * h
        guard rh > 2 else { continue }
        let font = CTFontCreateWithName(fontName, rh * 0.80, nil)
        let attr = NSAttributedString(string: c.string, attributes: [.font: font])
        let line = CTLineCreateWithAttributedString(attr)
        ctx.textPosition = CGPoint(x: x, y: y)
        CTLineDraw(line, ctx)
    }
    ctx.restoreGState()
    ctx.endPDFPage()
    FileHandle.standardError.write("page \(i+1)/\(last)\r".data(using: .utf8)!)
}
ctx.closePDF()
FileHandle.standardError.write("\n".data(using: .utf8)!)
