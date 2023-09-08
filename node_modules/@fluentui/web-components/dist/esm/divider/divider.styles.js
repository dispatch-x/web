import { css } from '@microsoft/fast-element';
import { display } from '@microsoft/fast-foundation';
import { designUnit, neutralStrokeDividerRest, strokeWidth } from '../design-tokens';
export const dividerStyles = (context, definition) => css `
    ${display('block')} :host {
      box-sizing: content-box;
      height: 0;
      border: none;
      border-top: calc(${strokeWidth} * 1px) solid ${neutralStrokeDividerRest};
    }

    :host([orientation="vertical"]) {
      border: none;
      height: 100%;
      margin: 0 calc(${designUnit} * 1px);
      border-left: calc(${strokeWidth} * 1px) solid ${neutralStrokeDividerRest};
  }
  `;
