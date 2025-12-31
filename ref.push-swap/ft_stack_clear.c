/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_stack_clear.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: agiron-d <agiron-d@student.42urduliz.co    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/27 17:10:16 by agiron-d          #+#    #+#             */
/*   Updated: 2025/11/27 17:11:32 by agiron-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_stack_clear(t_stack **stack)
{
	t_stack	*current;
	t_stack	*next;
	int		size;
	int		i;

	if (!stack || !*stack)
		return ;
	size = ft_stack_size(*stack);
	current = *stack;
	i = 0;
	while (i < size)
	{
		next = current->next;
		free(current);
		current = next;
		i++;
	}
	*stack = NULL;
}
