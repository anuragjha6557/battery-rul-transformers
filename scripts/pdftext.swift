import Foundation
import PDFKit

let args = CommandLine.arguments
guard args.count > 1, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: pdftext <file.pdf>\n".data(using: .utf8)!)
    exit(1)
}
for i in 0..<doc.pageCount {
    print("\n===== PAGE \(i + 1) =====\n")
    print(doc.page(at: i)?.string ?? "")
}
