# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""PDF utility functions."""

import io

from PyPDF2 import PdfReader, PdfWriter


def get_pdf_page_bytes(pdf_bytes_io: io.BytesIO, page_number: int) -> bytes:
    """Get the PDF bytes for a single PDF page."""
    pdf_file_reader = PdfReader(stream=pdf_bytes_io, strict=False)
    pdf_file_writer = PdfWriter()

    page = pdf_file_reader.pages[page_number - 1]
    pdf_file_writer.add_page(page=page)

    pdf_page_bytes_io = io.BytesIO()
    pdf_file_writer.write(pdf_page_bytes_io)
    page_bytes = pdf_page_bytes_io.getvalue()

    print(f"Length of bytes for page_number {page_number}: {len(page_bytes)}")
    return page_bytes


def get_pdf_bytes(path_to_pdf: str) -> bytes:
    """Get bytes for local PDF file."""
    pdf_file = open(path_to_pdf, 'rb')
    pdf_file_content_bytes = pdf_file.read()
    pdf_file.close()
    return pdf_file_content_bytes
